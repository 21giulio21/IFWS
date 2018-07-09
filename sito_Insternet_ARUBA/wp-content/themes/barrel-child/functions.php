<?php
add_action( 'wp_enqueue_scripts', 'barrel_enqueue_styles' );
function barrel_enqueue_styles() {
    wp_enqueue_style( 'bootstrap', get_template_directory_uri() . '/css/bootstrap.css' );
    wp_enqueue_style( 'barrel-parent-style', get_template_directory_uri() . '/style.css', array('bootstrap'));
    wp_enqueue_style( 'barrel-child-style', get_stylesheet_directory_uri() . '/style.css', array('bootstrap'));
} 
?>