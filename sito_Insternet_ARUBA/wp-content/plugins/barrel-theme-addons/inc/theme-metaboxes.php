<?php
/**
 * Theme custom metaboxes
 **/

/**
 * Page settings metabox
 */
if (!function_exists('barrel_pages_settings_box')) :
function barrel_pages_settings_box() {

    $screens = array('page');

    foreach ( $screens as $screen ) {

        add_meta_box(
            'barrel_pages_settings_box',
            esc_html__( 'Page settings', 'barrel-ta' ),
            'barrel_pages_settings_inner_box',
            $screen,
            'normal',
            'high'
        );
    }
}
endif;
add_action( 'add_meta_boxes', 'barrel_pages_settings_box' );

if (!function_exists('barrel_pages_settings_inner_box')) :
function barrel_pages_settings_inner_box( $post ) {

  wp_enqueue_script('wp-color-picker');
  wp_enqueue_style( 'wp-color-picker' );

  // Add an nonce field so we can check for it later.
  wp_nonce_field( 'barrel_pages_settings_inner_box', 'barrel_pages_settings_inner_box_nonce' );

  /*
   * Use get_post_meta() to retrieve an existing value
   * from the database and use the value for the form.
   */
  $value_page_class = get_post_meta( $post->ID, '_page_class_value', true );
  $value_page_bgcolor = get_post_meta( $post->ID, '_page_bgcolor_value', true );

  $value_page_notdisplaytitle = get_post_meta( $post->ID, '_page_notdisplaytitle_value', true );

  $value_page_stick_footer = get_post_meta( $post->ID, '_page_stick_footer_value', true );

  $value_page_transparent_header = get_post_meta( $post->ID, '_page_transparent_header_value', true );

  $value_page_sidebarposition = get_post_meta( $post->ID, '_page_sidebarposition_value', true );

  echo '<label for="page_class" style="width: 130px; display:inline-block;">';
       esc_html_e( "Page CSS class: ", 'barrel-ta' );
  echo '</label> ';
  echo '<input type="text" id="page_class" name="page_class" value="' . esc_attr( $value_page_class ) . '" style="width: 100%" />';
  
  $checked = '';
  if( $value_page_stick_footer == true ) { 
    $checked = 'checked = "checked"';
  }
  echo '<p><input type="checkbox" id="page_stick_footer" name="page_stick_footer" '.$checked.' /> <label for="page_stick_footer">'.esc_html__( "Stick page content to footer (disable page bottom margin)", 'barrel-ta' ).'</label></p>';

  $checked = '';
  if( $value_page_transparent_header == true ) { 
    $checked = 'checked = "checked"';
  }
  echo '<p><input type="checkbox" id="page_transparent_header" name="page_transparent_header" '.$checked.' /> <label for="page_transparent_header">'.esc_html__( "Show transparent header with light logo and white menus under page content. Use this if you have fullwidth image or slider at the page start (header will be displayed above your image).", 'barrel-ta' ).'</label></p>';


  $checked = '';
  if( $value_page_notdisplaytitle == true ) { 
    $checked = 'checked = "checked"';
  }
  echo '<p><input type="checkbox" id="page_notdisplaytitle" name="page_notdisplaytitle" '.$checked.' /> <label for="page_notdisplaytitle">'.esc_html__( "Don't display this page title (only show page content)", 'barrel-ta' ).'</label></p>';

  $selected_1 = '';
  $selected_2 = '';
  $selected_3 = '';
  $selected_4 = '';

  if($value_page_sidebarposition == 0) {
    $selected_1 = ' selected';
  }
  if($value_page_sidebarposition == "left") {
    $selected_2 = ' selected';
  }
  if($value_page_sidebarposition == "right") {
    $selected_3 = ' selected';
  }
  if($value_page_sidebarposition == "disable") {
    $selected_4 = ' selected';
  }
  
  echo '<p><label for="page_sidebarposition" style="display: inline-block; width: 150px;">'.esc_html__( "Page sidebar position: ", 'barrel-ta' ).'</label>';
  echo '<select name="page_sidebarposition" id="page_sidebarposition">
        <option value="0"'.$selected_1.'>'.esc_html__( "Use theme control panel settings", 'barrel-ta' ).'</option>
        <option value="left"'.$selected_2.'>'.esc_html__( "Left", 'barrel-ta' ).'</option>
        <option value="right"'.$selected_3.'>'.esc_html__( "Right", 'barrel-ta' ).'</option>
        <option value="disable"'.$selected_4.'>'.esc_html__( "Disable sidebar", 'barrel-ta' ).'</option>
    </select></p>';

  echo '<label for="page_bgcolor" style="display: inline-block; height: 40px;">'.esc_html__( "Page background color: ", 'barrel-ta' ).'</label> &nbsp;';
  echo '<input type="text" id="page_bgcolor" name="page_bgcolor" value="' . esc_attr( $value_page_bgcolor ) . '" style="width: auto; height:25px;" />';
 
  echo "<script type=\"text/javascript\">    jQuery(document).ready(function($) {    $('#page_bgcolor').wpColorPicker(); }); </script>";

}
endif;

if (!function_exists('barrel_page_settings_save_postdata')) :
function barrel_page_settings_save_postdata( $post_id ) {

  /*
   * We need to verify this came from the our screen and with proper authorization,
   * because save_post can be triggered at other times.
   */

  // Check if our nonce is set.
  if ( ! isset( $_POST['barrel_pages_settings_inner_box_nonce'] ) )
    return $post_id;

  $nonce = $_POST['barrel_pages_settings_inner_box_nonce'];

  // Verify that the nonce is valid.
  if ( ! wp_verify_nonce( $nonce, 'barrel_pages_settings_inner_box' ) )
      return $post_id;

  // If this is an autosave, our form has not been submitted, so we don't want to do anything.
  if ( defined( 'DOING_AUTOSAVE' ) && DOING_AUTOSAVE ) 
      return $post_id;

  // Check the user's permissions.
  if ( 'page' == $_POST['post_type'] ) {

    if ( ! current_user_can( 'edit_page', $post_id ) )
        return $post_id;
  
  } else {

    if ( ! current_user_can( 'edit_post', $post_id ) )
        return $post_id;
  }

  /* OK, its safe for us to save the data now. */

  // Sanitize user input.
  $mydata = sanitize_text_field( $_POST['page_class'] );

  // Update the meta field in the database.
  update_post_meta( $post_id, '_page_class_value', $mydata );

  // Sanitize user input.
  $mydata = sanitize_text_field( $_POST['page_bgcolor'] );

  // Update the meta field in the database.
  update_post_meta( $post_id, '_page_bgcolor_value', $mydata );

  // Sanitize user input.
  if(!isset($_POST['page_stick_footer'])) $_POST['page_stick_footer'] = false;
  
  $mydata = sanitize_text_field( $_POST['page_stick_footer'] );

  // Update the meta field in the database.
  update_post_meta( $post_id, '_page_stick_footer_value', $mydata );

  // Sanitize user input.
  if(!isset($_POST['page_transparent_header'])) $_POST['page_transparent_header'] = false;
  
  $mydata = sanitize_text_field( $_POST['page_transparent_header'] );

  // Update the meta field in the database.
  update_post_meta( $post_id, '_page_transparent_header_value', $mydata );

  // Sanitize user input.
  if(!isset($_POST['page_notdisplaytitle'])) $_POST['page_notdisplaytitle'] = false;
  
  $mydata = sanitize_text_field( $_POST['page_notdisplaytitle'] );

  // Update the meta field in the database.
  update_post_meta( $post_id, '_page_notdisplaytitle_value', $mydata );

  // Sanitize user input.
  $mydata = sanitize_text_field( $_POST['page_sidebarposition'] );

  // Update the meta field in the database.
  update_post_meta( $post_id, '_page_sidebarposition_value', $mydata );

}
endif;
add_action( 'save_post', 'barrel_page_settings_save_postdata' );

/**
 * Post settings metabox
 */
if (!function_exists('barrel_post_settings_box')) :
function barrel_post_settings_box() {

    $screens = array( 'post' );

    foreach ( $screens as $screen ) {

        add_meta_box(
            'barrel_post_settings_box',
            esc_html__( 'Post settings', 'barrel-ta' ),
            'barrel_post_settings_inner_box',
            $screen,
            'normal',
            'high'
        );
    }
}
endif;
add_action( 'add_meta_boxes', 'barrel_post_settings_box' );

if (!function_exists('barrel_post_settings_inner_box')) :
function barrel_post_settings_inner_box( $post ) {

  wp_enqueue_script('wp-color-picker');
  wp_enqueue_style( 'wp-color-picker' );

  // Add an nonce field so we can check for it later.
  wp_nonce_field( 'barrel_post_settings_inner_box', 'barrel_post_settings_inner_box_nonce' );

  /*
   * Use get_post_meta() to retrieve an existing value
   * from the database and use the value for the form.
   */
  $value_post_bgcolor = get_post_meta( $post->ID, '_post_bgcolor_value', true );
  $value_post_sidebarposition = get_post_meta( $post->ID, '_post_sidebarposition_value', true );

  $value_post_socialshare_disable = get_post_meta( $post->ID, '_post_socialshare_disable_value', true );
  $value_post_notdisplaytitle = get_post_meta( $post->ID, '_post_notdisplaytitle_value', true );
  $value_post_notdisplaythumbnail = get_post_meta( $post->ID, '_post_notdisplaythumbnail_value', true );
  $value_post_transparent_header = get_post_meta( $post->ID, '_post_transparent_header_value', true );


  $checked = '';
  if( $value_post_socialshare_disable == true ) { 
    $checked = 'checked = "checked"';
  }

  echo '<p><input type="checkbox" id="post_socialshare_disable" name="post_socialshare_disable" '.$checked.' /> <label for="post_socialshare_disable">'.esc_html__( "Disable social share counters and buttons on this post.", 'barrel-ta' ).'</label></p>';

  
  $checked = '';
  if( $value_post_notdisplaytitle == true ) { 
    $checked = 'checked = "checked"';
  }

  echo '<p><input type="checkbox" id="post_notdisplaytitle" name="post_notdisplaytitle" '.$checked.' /> <label for="post_notdisplaytitle">'.esc_html__( "Don't display this post title (only show page content).", 'barrel-ta' ).'</label></p>';

  $checked = '';
  if( $value_post_notdisplaythumbnail == true ) { 
    $checked = 'checked = "checked"';
  }

  echo '<p><input type="checkbox" id="post_notdisplaythumbnail" name="post_notdisplaythumbnail" '.$checked.' /> <label for="post_notdisplaythumbnail">'.esc_html__( "Don't display this post featured image on single post page.", 'barrel-ta' ).'</label></p>';


  $checked = '';
  if( $value_post_transparent_header == true ) { 
    $checked = 'checked = "checked"';
  }

  echo '<p><input type="checkbox" id="post_transparent_header" name="post_transparent_header" '.$checked.' /> <label for="post_transparent_header">'.esc_html__( "Show transparent header with light logo and white menus under page content. Use this if you have fullwidth image or slider at the page start (header will be displayed above your image).", 'barrel-ta' ).'</label></p>';


  $selected_1 = '';
  $selected_2 = '';
  $selected_3 = '';
  $selected_4 = '';

  if($value_post_sidebarposition == 0) {
    $selected_1 = ' selected';
  }
  if($value_post_sidebarposition == "left") {
    $selected_2 = ' selected';
  }
  if($value_post_sidebarposition == "right") {
    $selected_3 = ' selected';
  }
  if($value_post_sidebarposition == "disable") {
    $selected_4 = ' selected';
  }
  
  echo '<p><label for="post_sidebarposition" style="display: inline-block; width: 150px;">'.esc_html__( "Post sidebar position: ", 'barrel-ta' ).'</label>';
  echo '<select name="post_sidebarposition" id="post_sidebarposition">
        <option value="0"'.$selected_1.'>'.esc_html__( "Use theme control panel settings", 'barrel-ta' ).'</option>
        <option value="left"'.$selected_2.'>'.esc_html__( "Left", 'barrel-ta' ).'</option>
        <option value="right"'.$selected_3.'>'.esc_html__( "Right", 'barrel-ta' ).'</option>
        <option value="disable"'.$selected_4.'>'.esc_html__( "Disable sidebar", 'barrel-ta' ).'</option>
    </select></p>';

  echo '<label for="post_bgcolor" style="display: inline-block; height: 40px;">'.esc_html__( "Post background color: ", 'barrel-ta' ).'</label> &nbsp;';
  echo '<input type="text" id="post_bgcolor" name="post_bgcolor" value="' . esc_attr( $value_post_bgcolor ) . '" style="width: auto; height:25px;" />';
 
  echo "<script type=\"text/javascript\">    jQuery(document).ready(function($) {    $('#post_bgcolor').wpColorPicker(); }); </script>";

}
endif;

if (!function_exists('barrel_post_settings_save_postdata')) :
function barrel_post_settings_save_postdata( $post_id ) {

  /*
   * We need to verify this came from the our screen and with proper authorization,
   * because save_post can be triggered at other times.
   */

  // Check if our nonce is set.
  if ( ! isset( $_POST['barrel_post_settings_inner_box_nonce'] ) )
    return $post_id;

  $nonce = $_POST['barrel_post_settings_inner_box_nonce'];

  // Verify that the nonce is valid.
  if ( ! wp_verify_nonce( $nonce, 'barrel_post_settings_inner_box' ) )
      return $post_id;

  // If this is an autosave, our form has not been submitted, so we don't want to do anything.
  if ( defined( 'DOING_AUTOSAVE' ) && DOING_AUTOSAVE ) 
      return $post_id;

  // Check the user's permissions.
  if ( 'page' == $_POST['post_type'] ) {

    if ( ! current_user_can( 'edit_page', $post_id ) )
        return $post_id;
  
  } else {

    if ( ! current_user_can( 'edit_post', $post_id ) )
        return $post_id;
  }

  /* OK, its safe for us to save the data now. */

  // Sanitize user input.
  $mydata = sanitize_text_field( $_POST['post_bgcolor'] );

  // Update the meta field in the database.
  update_post_meta( $post_id, '_post_bgcolor_value', $mydata );

  // Sanitize user input.
  $mydata = sanitize_text_field( $_POST['post_sidebarposition'] );

  // Update the meta field in the database.
  update_post_meta( $post_id, '_post_sidebarposition_value', $mydata );

  if(!isset($_POST['post_socialshare_disable'])) $_POST['post_socialshare_disable'] = false;
  
   // Sanitize user input.
  $mydata = sanitize_text_field( $_POST['post_socialshare_disable'] );

  // Update the meta field in the database.
  update_post_meta( $post_id, '_post_socialshare_disable_value', $mydata );


  if(!isset($_POST['post_notdisplaytitle'])) $_POST['post_notdisplaytitle'] = false;
  
   // Sanitize user input.
  $mydata = sanitize_text_field( $_POST['post_notdisplaytitle'] );

  // Update the meta field in the database.
  update_post_meta( $post_id, '_post_notdisplaytitle_value', $mydata );

  if(!isset($_POST['post_notdisplaythumbnail'])) $_POST['post_notdisplaythumbnail'] = false;
  
   // Sanitize user input.
  $mydata = sanitize_text_field( $_POST['post_notdisplaythumbnail'] );

  // Update the meta field in the database.
  update_post_meta( $post_id, '_post_notdisplaythumbnail_value', $mydata );  

  if(!isset($_POST['post_transparent_header'])) $_POST['post_transparent_header'] = false;
  
   // Sanitize user input.
  $mydata = sanitize_text_field( $_POST['post_transparent_header'] );

  // Update the meta field in the database.
  update_post_meta( $post_id, '_post_transparent_header_value', $mydata );  

}
endif;
add_action( 'save_post', 'barrel_post_settings_save_postdata' );

// CMD2 MetaBoxes
if (!function_exists('barrel_register_post_settings_metabox')) :
function barrel_register_post_settings_metabox() {

  // Start with an underscore to hide fields from custom fields list
  $prefix = '_barrel_';
  /**
   * Metabox to be displayed on a single page ID
   */
  $cmb_post_header_settings = new_cmb2_box( array(
    'id'           => $prefix . 'post_header_settings_metabox',
    'title'        => esc_html__( 'Title Background settings', 'barrel-ta' ),
    'object_types' => array( 'post', 'page', 'mgt_portfolio' ), // Post type
    'context'      => 'normal',
    'priority'     => 'high',
    'show_names'   => true, // Show field names on the left
  ) );
  $cmb_post_header_settings->add_field( array(
    'name'         => esc_html__( 'Title Background Image', 'barrel-ta' ),
    'desc'         => esc_html__( 'You can display fullwidth image background in your post/page header with post title. Use wide image here.', 'barrel-ta' ),
    'id'           => $prefix . 'header_image',
    'type'         => 'file',
    'options' => array(
        'url' => false, // Hide the text input for the url
        'add_upload_file_text' => 'Select or Upload Image' 
    ),
    'preview_size' => array( 100, 100 ), // Default: array( 50, 50 )
  ) );

  $cmb_post_header_settings->add_field( array(
    'name'    => 'Title Background Color',
    'id'      => $prefix . 'header_bgcolor',
    'desc'         => esc_html__( 'You can change post/page title background here.', 'barrel-ta' ),
    'type'    => 'colorpicker',
    'default' => '',
  ) );
  
}
endif;
add_action( 'cmb2_init', 'barrel_register_post_settings_metabox' );