<?php
/**
 * WP Theme Header
 *
 * Displays all of the <head> section
 *
 * @package Barrel
 */
$barrel_theme_options = barrel_get_theme_options();

// Demo settings
if ( defined('DEMO_MODE') && isset($_GET['header_logo_position']) ) {
  $barrel_theme_options['header_logo_position'] = esc_html($_GET['header_logo_position']);
}
if ( defined('DEMO_MODE') && isset($_GET['header_fullwidth']) ) {
  if($_GET['header_fullwidth'] == 0) {
    $barrel_theme_options['header_fullwidth'] = false;
  }
  if($_GET['header_fullwidth'] == 1) {
    $barrel_theme_options['header_fullwidth'] = true;
  }

}
?><!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta charset="<?php bloginfo( 'charset' ); ?>" />
<link rel="profile" href="http://gmpg.org/xfn/11" />
<link rel="pingback" href="<?php bloginfo( 'pingback_url' ); ?>">
<?php wp_head(); ?>
</head>

<body <?php echo body_class(); ?>>

<?php
// Progress bar
if(isset($barrel_theme_options['enable_progressbar']) && $barrel_theme_options['enable_progressbar']): ?>
<div class="header-progressbar">
    <div class="header-progressbar-under-bar"></div>
</div>
<?php endif; ?>

<?php
// Use menu below header if you use center logo layout
if(isset($barrel_theme_options['header_logo_position']) && $barrel_theme_options['header_logo_position'] == 'center') {
  $barrel_theme_options['header_menu_layout'] = 'menu_below_header';
}

// Don't show special header menu layout depending on settings
if(isset($barrel_theme_options['header_menu_layout']) && $barrel_theme_options['header_menu_layout'] == "menu_below_header" ) {
  $barrel_theme_options['top_menu_position'] = "default";
}

if(isset($barrel_theme_options['top_menu_position']) && $barrel_theme_options['top_menu_position'] == "header" ) {
  $barrel_theme_options['header_logo_position'] = "left";
}

// Center logo
if(isset($barrel_theme_options['header_logo_position']) && $barrel_theme_options['header_logo_position'] == 'center') {
  $header_container_add_class = ' header-logo-center';
} else {
  $header_container_add_class = '';
}
if(isset($barrel_theme_options['header_fullwidth']) && $barrel_theme_options['header_fullwidth']) {
  $header_container_class = 'container-fluid';
} else {
  $header_container_class = 'container';
}

// Sticky header
if(isset($barrel_theme_options['enable_sticky_header']) && $barrel_theme_options['enable_sticky_header']) {
  $header_add_class = 'sticky-header main-header';
} else {
  $header_add_class = 'main-header';
}

// Sticky header elements
if(!isset($barrel_theme_options['sticky_header_elements'])) {
  $barrel_theme_options['sticky_header_elements'] = 'headeronly';
}

$header_add_class .= ' sticky-header-elements-'.esc_attr($barrel_theme_options['sticky_header_elements']);

$header_add_class .= ' mainmenu-position-'.esc_attr($barrel_theme_options['header_menu_layout']);

?>
<?php     
// Left header
if(isset($barrel_theme_options['header_position']) && $barrel_theme_options['header_position'] == 'left'):
?>
<header class="left-side-header">
<?php barrel_header_side_show(); ?>
</header>
<?php else: ?>
<?php barrel_menu_top_show(); ?>
<header class="<?php echo esc_attr($header_add_class); ?>">
<div class="<?php echo esc_attr($header_container_class); ?><?php echo esc_attr($header_container_add_class); ?>">
  <div class="row">
    <div class="col-md-12">
     
      <div class="header-left">
          <?php barrel_header_left_show(); ?>
      </div>
      
      <div class="header-center">
        <?php barrel_header_center_show(); ?>
      </div>
      
      <div class="header-right">
        <?php barrel_header_right_show(); ?>
      </div>

    </div>
  </div>
    
</div>
<?php barrel_menu_below_header_show(); ?>
</header>
<?php endif; ?>