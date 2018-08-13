<?php
/**
 * Frontend Reset Password - Functions
 *
 * @version	1.0.5
 */
session_start();
if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

add_action( 'init', 'somfrp_load_lang' );
function somfrp_load_lang() {
	$lang_dir = SOMFRP_PATH  . 'i18n/languages';
	load_plugin_textdomain( 'frontend-reset-password', false, $lang_dir );
}

add_action( 'wp_enqueue_scripts', 'somfrp_lost_password_style' );
function somfrp_lost_password_style() {
	wp_register_style( 'som_lost_password_style', plugins_url( '/assets/css/password-lost.css', dirname(__FILE__) ) );
	wp_enqueue_style( 'som_lost_password_style' );
	$som_reset_password_script = plugins_url( 'assets/js/password-lost.js', dirname(__FILE__) );
	wp_enqueue_script( 'som_reset_password_script', $som_reset_password_script, array( 'jquery' ), '1.0.0', true );
}

add_action( 'admin_enqueue_scripts', 'somfrp_admin_scripts' );
function somfrp_admin_scripts() {
	wp_enqueue_script( 'somfrp-admin-script', plugins_url('/assets/js/password-lost-admin.js',  dirname( __FILE__ ) ), array( 'jquery', 'wp-color-picker' ) , '1.0.0', true );
	wp_enqueue_style( 'wp-color-picker' );
}

add_action( 'wp_head', 'somfrp_colour_css' );
function somfrp_colour_css() {
	$options = get_option( 'somfrp_gen_settings' );
	$colour = ( isset( $options['somfrp_notice_bg'] ) && $options['somfrp_notice_bg'] ) ? $options['somfrp_notice_bg']: '' ;
	if ( ! empty( $colour ) ) {
		echo '<style>
.som-password-error-message,
.som-password-sent-message {
	background-color: ' . $colour . ';
	border-color: ' . $colour . ';
}
</style>
';
	}
}

function som_get_login_url() {
	$options = get_option( 'somfrp_gen_settings' );
	$value = ( isset( $options['somfrp_login_page'] ) && $options['somfrp_login_page'] ) ? $options['somfrp_login_page']: '' ;
	if ( ! empty( $value ) ) {
		$page = esc_url( get_permalink( $value ) );
	} else {
		$page = esc_url( wp_login_url() );
	}
	return $page;
}

function som_get_register_url() {
	return get_permalink( get_page_by_path( 'login' ) ) . '?section=register';
}

function som_get_lost_password_url() {
	$options = get_option( 'somfrp_gen_settings' );
	$value = ( isset( $options['somfrp_reset_page'] ) && $options['somfrp_reset_page'] ) ? $options['somfrp_reset_page']: '' ;
	if ( ! empty( $value ) ) {
		$page = get_permalink( $value );
		return $page;
	}
}

add_filter( 'lostpassword_url', 'somfrp_custom_lostpassword_url', 99, 2 );
function somfrp_custom_lostpassword_url( $lostpassword_url, $redirect ) {
	$options = get_option( 'somfrp_gen_settings' );
	$value = ( isset( $options['somfrp_reset_page'] ) && $options['somfrp_reset_page'] ) ? $options['somfrp_reset_page']: '' ;
	if ( ! empty( $value ) ) {
		$page = get_permalink( $value );
		$lostpassword_url = $page;
	}
	return $lostpassword_url;
}

add_shortcode( 'reset_password', 'somfrp_reset_password_shortcode' );
function somfrp_reset_password_shortcode( $atts ) {

	// Attributes
	$atts = shortcode_atts(
		array(
		),
		$atts
	);

	return somfrp_render_lost_password_form();

}

function somfrp_render_lost_password_form() {
	if ( is_user_logged_in() ) {
		return __( 'You are already signed in.', 'frontend-reset-password' );
	}
	return somfrp_get_template_html( 'lost_password_form' );
}

function somfrp_get_template_html( $template_name ) {

	ob_start();

	//som_ar($_REQUEST);

	$errors = isset( $_REQUEST['errors'] ) ? $_REQUEST['errors'] : array() ;
	$url = isset( $_REQUEST['reset_url'] ) ? $_REQUEST['reset_url'] : '' ;

	do_action( 'somfrp_before_form' );

	// Grab the form output content settings
	$gen_options = get_option( 'somfrp_gen_settings' );
	$sec_options = get_option( 'somfrp_security_settings' );

	$min_length = ( isset( $sec_options['somfrp_pass_length'] ) && $sec_options['somfrp_pass_length'] )
		? esc_html( $sec_options['somfrp_pass_length'] )
		: '' ;

	$form_title = ( isset( $gen_options['somfrp_reset_form_title'] ) && $gen_options['somfrp_reset_form_title'] )
		? esc_html( $gen_options['somfrp_reset_form_title'] )
		: __( 'Reset Password', 'frontend-reset-password' ) ;

	$lost_text = ( isset( $gen_options['somfrp_reset_lost_message'] ) && $gen_options['somfrp_reset_lost_message'] )
		? $gen_options['somfrp_reset_lost_message']
		: '' ;

	if ( empty( $lost_text ) ) {
		$lost_text = __( 'Please enter your email address or username. You will receive a link to create a new password via email.', 'frontend-reset-password' );
		$lost_text_output = '<p class="extra-space">' . $lost_text . '</p>';
	} else {
		$allowed_tags = somfrp_get_allowed_html_tags();
		$lost_text_output = wpautop( wp_kses( $lost_text, $allowed_tags ) );
	}

	if ( empty( $min_length ) ) {

		$reset_text = ( isset( $gen_options['somfrp_reset_new_message'] ) && $gen_options['somfrp_reset_new_message'] )
			? $gen_options['somfrp_reset_new_message']
			: '' ;

		if ( empty( $reset_text ) ) {
			$reset_text = __( 'Please enter a new password.', 'frontend-reset-password' );
			$reset_text_output = '<p class="extra-space">' . $reset_text . '</p>';
		} else {
			$allowed_tags = somfrp_get_allowed_html_tags();
			$reset_text_output = wpautop( wp_kses( $reset_text, $allowed_tags ) );
		}

	} else {

		$reset_text = ( isset( $gen_options['somfrp_reset_new_message'] ) && $gen_options['somfrp_reset_new_message'] )
			? $gen_options['somfrp_reset_new_message']
			: '' ;

		if ( empty( $reset_text ) ) {
			$reset_text = sprintf( __( 'Please enter a new password. Minimum %s characters.', 'frontend-reset-password' ), $min_length );
			$reset_text_output = '<p class="extra-space">' . $reset_text . '</p>';
		} else {
			$allowed_tags = somfrp_get_allowed_html_tags();
			$reset_text_output = wpautop( wp_kses( $reset_text, $allowed_tags ) );
		}

	}

	$button_text = ( isset( $gen_options['somfrp_reset_button_text'] ) && $gen_options['somfrp_reset_button_text'] )
		? esc_html( $gen_options['somfrp_reset_button_text'] )
		: __( 'Reset Password', 'frontend-reset-password' ) ;


	// If checks to determine which template/form to show the user
	if ( isset( $_GET['somresetpass'] ) && ( isset( $_GET['action'] ) && $_GET['action'] == 'rp' ) )
	{
		echo "FOULONE";

		$key = trim( $_GET['key'] );
		$login = trim( $_GET['login'] );
		echo "login ".$login;

		//$user = check_password_reset_key( $key, $login );
		echo "GINO ". $user;
		$response = get_user_by("@",$_SESSION["email"]);
		echo "CANNOLO " . $response;

		if ( $response) {
			echo "RUGO";

			if ( $user->get_error_code() === 'expired_key' ) {

				$errors['expired_key'] = __( 'That key has expired. Please reset your password again.', 'frontend-reset-password' );

			} else {

				echo 'Error code:<br>';
				echo $user->get_error_code();
				exit;

				$errors['invalid_key'] = __( 'That key is no longer valid. Please reset your password again.', 'frontend-reset-password' );

			}

			require( SOMFRP_PATH . 'templates/lost_password_form.php' );

		} else {

			require( SOMFRP_PATH . 'templates/lost_password_reset_form.php' );

		}

	} elseif ( isset( $_GET['som_password_reset'] ) ) {

		require( SOMFRP_PATH . 'templates/lost_password_reset_complete.php' );

	} else {

		require( SOMFRP_PATH . 'templates/lost_password_form.php' );

	}

	do_action( 'somfrp_after_form' );

	$html = ob_get_contents();
	ob_end_clean();

	return $html;

}

add_action( 'template_redirect', 'somfrp_post_request', 99 );
function somfrp_post_request() {
	// Bail if not a POST action
	if ( ! somfrp_is_post_request() )
		return;

	// Bail if no action
	if ( empty( $_POST['action'] ) )
		return;

	// Use this static action if you don't mind checking the 'action' yourself.
	do_action( 'somfrp_post_request', $_POST['action'] );
}

add_action( 'somfrp_post_request', 'somfrp_lost_pass_handler', 50 );
function somfrp_lost_pass_handler( $action = '' ) {

	// Bail if action is not som_reset_pass
	if ( 'somfrp_lost_pass' !== $action )
		return;

	if ( ! somfrp_verify_nonce_request( 'somfrp_lost_pass' ) )
		somfrp_wp_error( '<strong>ERROR</strong>: ' . __( 'something went wrong with that!', 'frontend-reset-password' ) );

	$errors = array();

	$user_info = trim( $_POST['somfrp_user_info'] );

	if ( isset( $user_info ) && ! empty( $user_info ) )
	{

		if ( strpos( $user_info, '@' ) ) {
			$user_data = get_user_by( 'email', $user_info );
			if ( empty( $user_data ) )
			{
				$errors['no_email'] = __( 'That email address is not recognised.', 'frontend-reset-password' );
			}
		} else {

		}

	} else {

		$errors['invalid_input'] = __( 'Please enter a username or email address.', 'frontend-reset-password' );

	}

	if ( ! empty( $errors ) ) {
		$_REQUEST['errors'] = $errors;
		return;
	}

	do_action( 'somfrp_lost_pass_action', $user_info );

}
/*
Funzione definita da me che mi permette di prendere come input:
1) Modalità di ottenere lo user -> con email o username
2) Informazioni utili a ottenere lo user
Controllo se la mail è nel database oppure no. Nel caso non sia nel database la funzione non deve tornare nulla.
Se è nel database deve tornare qualcosa.

'login', $user_info

*/
function get_user_by($modo,$user_info)
{
	print_r("EMAIL ".$user_info);
	$_SESSION["email"] = $user_info;

	// Tolgo gli spazi e tolgo gli acapi da $_SESSION["email"]
	$_SESSION["email"] = str_replace(' ', '', $_SESSION["email"]);
	$_SESSION["email"] = str_replace('\n', '', $_SESSION["email"]);


	$target_url = "http://2.230.243.113/instagram/app/reset-password/checkIfEmailIsIntoDatabase.php";
  $params =
   array(
     "EMAIL" => $_SESSION["email"]

   );
	 $response = curl_request_custom($target_url,$params);
	 $response_json = json_decode($response)->success;
	 if($response_json == "success")
	 {
		 return true;
	 }else
	 {
		 return false;
	 }



}

function curl_request_custom($target_url, array $arguments){

	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL,$target_url);
	curl_setopt($ch, CURLOPT_POST, 1);
	curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($arguments));

	// receive server response ...
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	$server_output = curl_exec ($ch)or die("Errore nella curl_exec");
	curl_close ($ch);
	return $server_output;

}
add_action( 'somfrp_lost_pass_action', 'somfrp_lost_pass_callback' );
function somfrp_lost_pass_callback() {

	$errors = array();

	//We shall SQL escape all inputs to avoid sql injection.
	$user_info = trim( $_POST['somfrp_user_info'] );

	if ( empty( $user_info ) ) {

		// If the user has entered nothing in the form

		somfrp_wp_error( '<strong>ERROR</strong>: ' . __( 'Please add your email address or username!', 'frontend-reset-password' ) );
		exit;

	} elseif ( strpos( $user_info, '@' ) ) {

		// If the user has entered an email address into the form
/*
		$user_data = get_user_by( 'email', $user_info );
		if ( empty( $user_data ) ) {
			somfrp_wp_error( '<strong>ERROR</strong>: ' . __( 'No email address found!', 'frontend-reset-password' ) );
			exit;
		}
*/
	} else {

		// If the user has entered a username into the form

	}

	/**
	 * Fires before errors are returned from a password reset request.
	 *
	 * @since 2.1.0
	 * @since 4.4.0 Added the `$errors` parameter.
	 *
	 * @param WP_Error $errors A WP_Error object containing any errors generated
	 *                         by using invalid credentials.
	 */
	do_action( 'lostpassword_post' );

	// Redefining user_login ensures we return the right case in the email.
	$user_login = $_SESSION["email"];
	$key = get_password_reset_key( $user_data );

	if ( is_wp_error( $key ) ) {
		somfrp_wp_error( '<strong>ERROR</strong>: ' . __( 'key not found!', 'frontend-reset-password' ) );
		//return $key;
	}

	add_filter( 'wp_mail_content_type', 'somfrp_html_emails' );

	$reset_url = esc_url_raw( som_get_lost_password_url() . "?somresetpass=true&action=rp&key=$key&login=" . rawurlencode( $user_login ) );
	$reset_link = '<a href="' . $reset_url . '">' . $reset_url . '</a>';

	$options = get_option( 'somfrp_gen_settings' );

	$email_body = isset( $options['somfrp_email_message'] ) ? $options['somfrp_email_message'] : '' ;
	$from_email_name = ( isset( $options['somfrp_from_name'] ) && $options['somfrp_from_name'] ) ? esc_html( trim( $options['somfrp_from_name'] ) ): '' ;
	$from_email_address = ( isset( $options['somfrp_email_address'] ) && $options['somfrp_email_address'] ) ? esc_html( trim( $options['somfrp_email_address'] ) ) : '' ;

	$allowed_tags = somfrp_get_allowed_html_tags();

	$message = '';

	if ( empty( $email_body ) ) {

		ob_start(); ?>

		<p><?php _e( 'Someone requested that the password be reset for the following account:', 'frontend-reset-password' ); ?></p>
		<p><?php printf( __( 'Username: %s', 'frontend-reset-password' ), $user_login ); ?></p>
		<p><?php _e( 'If this was a mistake, just ignore this email and nothing will happen.', 'frontend-reset-password' ); ?></p>
		<p><?php _e( 'To reset your password, visit the following address:', 'frontend-reset-password' ); ?></p>
		<p><?php echo $reset_link; ?></p>
		<?php

		$message = ob_get_clean();

	} else {

		$email_body_user = str_replace( "{username}", $user_login, $email_body );
		$email_body_link = str_replace( "{reset_link}", $reset_link, $email_body_user );
		$email_body = wpautop( wp_kses( $email_body_link, $allowed_tags ) );
		$message = $email_body;

	}

	//$message .= network_site_url("wp-login.php?action=rp&key=$key&login=" . rawurlencode($user_login), 'login') . "\r\n";

	// replace PAGE_ID with reset page ID $_GET['somresetpass']

	$title = __( 'Account Password Reset', 'frontend-reset-password' );

	/**
	 * Filter the subject of the password reset email.
	 *
	 * @since 2.8.0
	 * @since 4.4.0 Added the `$user_login` and `$user_data` parameters.
	 *
	 * @param string  $title      Default email title.
	 * @param string  $user_login The username for the user.
	 * @param WP_User $user_data  WP_User object.
	 */
	$title = apply_filters( 'retrieve_password_title', $title, $user_login, $user_data );

	/**
	 * Filter the message body of the password reset mail.
	 *
	 * @since 2.8.0
	 * @since 4.1.0 Added `$user_login` and `$user_data` parameters.
	 *
	 * @param string  $message    Default mail message.
	 * @param string  $key        The activation key.
	 * @param string  $user_login The username for the user.
	 * @param WP_User $user_data  WP_User object.
	 */
	$message = apply_filters( 'retrieve_password_message', $message, $key, $user_login, $user_data );

	$admin_email = get_bloginfo( 'admin_email' );
	$site_title = get_bloginfo( 'name' );

	$headers[] = 'Content-Type: text/html; charset=UTF-8';

	if ( ! empty( $from_email_name ) && ! empty( $from_email_address ) ) {
		$headers[] = 'From: ' . $from_email_name . ' <'  .$from_email_address . '>';
	}

	$email_sent = false;

	if ( wp_mail( $_SESSION["email"], wp_specialchars_decode( $title ), $message, $headers ) ) {
		$email_sent = true;
		$_REQUEST['email_confirmed'] = __( 'An email has been sent. Please check your inbox.' , 'frontend-reset-password' );
		//$errors['password_email_not_sent'] = 'The e-mail could not be sent.';
	} else {
		$errors['password_email_not_sent'] = __( 'The e-mail could not be sent.', 'frontend-reset-password' );
		//$_REQUEST['email_confirmed'] = 'Check your ' . $_SESSION["email"] . ' inbox for the confirmation link.';
	}

	//remove_filter( 'wp_mail_content_type', 'text/html' );

	$_REQUEST['errors'] = $errors;
	$_REQUEST['reset_url'] = $reset_url;

	remove_filter( 'wp_mail_content_type', 'somfrp_html_emails' );

	if ( $email_sent ) {
		$options = get_option( 'somfrp_gen_settings' );
		$email_sent_page = ( isset( $options['somfrp_request_success_page'] ) && $options['somfrp_request_success_page'] )
		? get_permalink( intval( $options['somfrp_request_success_page'] ) )
		: '' ;
		if ( ! empty( $email_sent_page ) ) {
			wp_redirect( $email_sent_page );
			exit;
		}
	}

	return;

}

function somfrp_html_emails() {
	return 'text/html';
}

function somfrp_get_allowed_html_tags() {
	$allowed_tags = array(
		'a' => array(
			'href' => array(),
			'title' => array()
		),
		'p' => array(
			'style' => array()
		),
		'br' => array(),
		'em' => array(),
		'strong' => array(),
	);
	return apply_filters( 'somfrp_get_allowed_html_tags', $allowed_tags );
}

add_action( 'somfrp_post_request', 'somfrp_reset_pass_handler', 10 );
function somfrp_reset_pass_handler( $action = '' ) {

	// Bail if action is not som_reset_pass
	if ( 'somfrp_reset_pass' !== $action )
		return;

	if ( ! somfrp_verify_nonce_request( 'somfrp_reset_pass' ) )
		somfrp_wp_error( '<strong>ERROR</strong>: ' . __( 'something went wrong with that!', 'frontend-reset-password' ) );

	$errors = array();

	$user_pass = trim( $_POST['som_new_user_pass'] );
	$user_pass_repeat = trim( $_POST['som_new_user_pass_again'] );

	if ( empty( $user_pass ) || empty( $user_pass_repeat ) )
	{
		$errors['no_password'] = __( 'Please enter a new password.', 'frontend-reset-password' );
		$_REQUEST['errors'] = $errors;
		return;
	} elseif ( $user_pass !== $user_pass_repeat ) {
		$errors['password_mismatch'] = __( 'The passwords don\'t match.', 'frontend-reset-password' );
		$_REQUEST['errors'] = $errors;
		return;
	}

	$key = trim( $_GET['key'] );
	$login = trim( $_GET['login'] );

	if ( empty( $key ) || empty( $login ) ) {
		$errors['key_login'] = __( 'The reset link is not valid.', 'frontend-reset-password' );
		$_REQUEST['errors'] = $errors;
		wp_redirect( som_get_lost_password_url() );
		exit;
		// For good measure
		return;
	}

//Caso in cui tutto sia ok!
	if(strlen($user_pass)>7)
	{

			echo "Modifico ";
			echo "\n email da mandare: ".$_GET['login'];
			$target_url = "http://2.230.243.113/instagram/app/reset-password/setPasswordIntoDatabase.php";
		  $params =
		   array(
		     "EMAIL" => $_GET['login'] ,
				 "PASSWORD_SITE" => $user_pass

		   );
			 $response = curl_request_custom($target_url,$params);
			 echo $response;
			
	}





	if ( ! empty( $errors ) ) {
		$_REQUEST['errors'] = $errors;
		return;
	}

	do_action( 'somfrp_reset_pass_action', $user, $user_pass );

}

function setNewPasswordToUser()
{



}

add_action( 'somfrp_reset_pass_action', 'somfrp_reset_pass_callback', 10, 2 );
function somfrp_reset_pass_callback( $user, $user_pass ) {

	/**
	 * Fires before the password reset procedure is validated.
	 *
	 * @since 3.5.0
	 *
	 * @param object           $errors WP Error object.
	 * @param WP_User|WP_Error $user   WP_User object if the login and reset key match. WP_Error object otherwise.
	 */
	do_action( 'validate_password_reset', new WP_Error(), $user );

	reset_password( $user, $user_pass );

	$options = get_option( 'somfrp_gen_settings' );
	$reset_success_page = ( isset( $options['somfrp_reset_success_page'] ) && $options['somfrp_reset_success_page'] )
	? get_permalink( intval( $options['somfrp_reset_success_page'] ) )
	: som_get_lost_password_url() . '?som_password_reset=true' ;

	wp_redirect( $reset_success_page );
	exit;

}

function somfrp_is_post_request() {
	return (bool) ( 'POST' === strtoupper( $_SERVER['REQUEST_METHOD'] ) );
}

function somfrp_verify_nonce_request( $action = '', $query_arg = 'somfrp_nonce' ) {

	// Check the nonce
	$result = isset( $_REQUEST[$query_arg] ) ? wp_verify_nonce( $_REQUEST[$query_arg], $action ) : false;

	// Nonce check failed
	if ( empty( $result ) || empty( $action ) ) {
		$result = false;
	}

	// Do extra things
	do_action( 'somfrp_verify_nonce_request', $action, $result );

	return $result;
}

function somfrp_wp_error( $message, $args = array() ) {
	$error = new WP_Error( 'somfrp_error', $message );
	$site_title = get_bloginfo( 'name' );
	wp_die( $error, $site_title . ' - Error', $args );
}
