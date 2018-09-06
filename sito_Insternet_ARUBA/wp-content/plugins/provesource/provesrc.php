<?php
/**
 * @package: provesrc-plugin
 */

/**
 * Plugin Name: ProveSource
 * Description: ProveSource is a social proof marketing platform that works with your Wordpress and WooCommerce websites out of the box
 * Version: 1.0.5
 * Author: ProveSource LTD
 * Author URI: https://provesrc.com
 * License: GPLv3 or later
 * Text Domain: provesrc-plugin
 */

if (!defined('ABSPATH')) {
    die;
}

/** constants */
class PSConstants {
	public static function options_group() {
		return 'provesrc_options';
	}

	public static function option_api_key() {
		return 'api_key';
	}
}

/** hooks */
add_action('admin_menu', 'provesrc_admin_menu'); //1.5.0
add_action('admin_init', 'provesrc_admin_init'); //2.5.0
add_action('admin_notices', 'provesrc_admin_notice_html'); //3.1.0
add_action('wp_head', 'provesrc_inject_code'); //1.2.0
// add_action('woocommerce_checkout_create_order', 'provesrc_woocommerce_order_created', 20, 2);
add_action('woocommerce_checkout_order_processed', 'provesrc_order_processed');

function provesrc_admin_menu() {
	add_menu_page('ProveSource Settings', 'ProveSource', 'manage_options', 'provesrc', 'provesrc_menu_page_html', 'dashicons-provesrc');
}

function provesrc_admin_init() {
	wp_enqueue_style('provesrc_admin_style', plugin_dir_url(__FILE__) . 'style.css' );
	register_setting(PSConstants::options_group(), PSConstants::option_api_key());
	wp_register_style('dashicons-provesrc', plugin_dir_url(__FILE__) . '/assets/css/dashicons-provesrc.css');
	wp_enqueue_style('dashicons-provesrc');
}

function provesrc_inject_code() {
	$apiKey = provesrc_get_api_key();
	?>

	<!-- Start of Async ProveSource Code (Wordpress) --><script>!function(o,i){window.provesrc&&window.console&&console.error&&console.error("ProveSource is included twice in this page."),provesrc=window.provesrc={dq:[],display:function(o,i){this.dq.push({n:o,g:i})}},o._provesrcAsyncInit=function(){provesrc.init({apiKey:"<?php echo $apiKey; ?>",v:"0.0.3"})};var r=i.createElement("script");r.type="text/javascript",r.async=!0,r.src="https://cdn.provesrc.com/provesrc.js";var e=i.getElementsByTagName("script")[0];e.parentNode.insertBefore(r,e)}(window,document);</script><!-- End of Async ProveSource Code -->

	<?php
}

function provesrc_order_processed($id) {
	$order = wc_get_order( $id );
	$items = $order->get_items();
	$products = array();
	foreach($items as $item) {
		$quantity = $item->get_quantity();
		$product = $item->get_product();
		$images_arr = wp_get_attachment_image_src( $product->get_image_id(), array('72', '72'), false );
		$image = null;
		if($images_arr !== null && $images_arr[0] !== null) $image = $images_arr[0];
		$p = array(
			'id' => $product->get_id(),
			'quantity' => (int)$quantity,
			'price' => (int)$product->get_price(),
			'name' => $product->get_name(),
			'link' => get_permalink($product->get_id()),
			'image' => $image
		);
		array_push($products, $p);
	}
	provesrc_send_webhook($order, $products);
}

function provesrc_send_webhook($order, $products) {
	$apiKey = provesrc_get_api_key();
	if(!isset($apiKey)) return;
	
	$headers = array(
		'Content-Type' => 'application/json',
		'authorization' => 'Bearer ' . $apiKey
	);
	$data = array(
		'firstName' => $order->get_billing_first_name(),
		'lastName' => $order->get_billing_last_name(),
		'email' => $order->get_billing_email(),
		'ip' => $order->get_customer_ip_address(),
		'siteUrl' => get_site_url(),
		'total' => (int)$order->get_total(),
		'currency' => $order->get_currency(),
		'products' => $products
	);
	$url = 'https://api.provesrc.com/webhooks/track/woocommerce';
	$res = wp_remote_post($url, array(
		'headers' => $headers,
		'body' => json_encode($data)
	));
}

/** helpers */

function provesrc_get_api_key() {
	$apiKey = get_option(PSConstants::option_api_key());
	if(isset($apiKey) && strlen($apiKey) > 30) return $apiKey;
	return null;
}

function provesrc_menu_page_html() {
	if (!current_user_can('manage_options')) {
		return;
	}
	
	?>

	<div class="wrap" id="ps-settings">
		<!-- <h1><?=esc_html(get_admin_page_title()); ?></h1> -->
		<a href="https://provesrc.com">
			<img class="top-logo" src="<?php echo plugin_dir_url(__FILE__) . "assets/top-logo.png" ?>">
		</a>
		<form action="options.php" method="post">

			<?php
				settings_fields(PSConstants::options_group());
				do_settings_sections(PSConstants::options_group());
			?>

			<div class="ps-settings-container">
				<div class="account-link">If you don't have an account - <a href="https://console.provesrc.com/?utm_source=woocommerce&utm_medium=plugin&utm_campaign=woocommerce-signup#/signup" target="_blank">signup here!</a></div>
				<div class="label">Your API Key:</div>
				<input type="text" placeholder="required" name="<?php echo PSConstants::option_api_key(); ?>" value="<?php echo esc_attr(get_option(PSConstants::option_api_key())); ?>" />
				<div class="m-t"><a href="https://console.provesrc.com/#/settings" target="_blank">Where is my API Key?</a></div>
			</div>

			<?php submit_button('Save'); ?>
		
        </form>
    </div>

    <?php
}

function provesrc_admin_notice_html() {
	$apiKey = provesrc_get_api_key();
	if($apiKey !== null) return;

	$screen = get_current_screen();
	if($screen !== null && strpos($screen->id, 'provesrc') > 0) return;

	?>

	<div class="notice notice-error is-dismissible">
        <p class="ps-error">ProveSource is not configured! <a href="admin.php?page=provesrc">Click here</a></p>
    </div>

	<?php
}

function provesrc_log($message, $data=null) {
	if(isset($data)) {
		if(is_array($data)) $data = implode(' | ', $data);
		error_log($message . ': ' . print_r($data, true));

	} else {
		error_log($message);
	}
}

?>
