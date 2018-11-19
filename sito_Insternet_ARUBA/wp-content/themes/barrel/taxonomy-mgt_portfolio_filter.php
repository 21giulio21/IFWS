<?php
/**
 * The template used for displaying mgt_portfolio_filter taxonomy page
 *
 * @package Barrel
 */

$barrel_theme_options = barrel_get_theme_options();

if(isset($barrel_theme_options['portfolio_page_url']) && $barrel_theme_options['portfolio_page_url']!=='') {
  $portfolio_page_url = $barrel_theme_options['portfolio_page_url'];
} else {
  $portfolio_page_url = home_url();
}

wp_redirect( esc_url($portfolio_page_url) ); exit;

?>