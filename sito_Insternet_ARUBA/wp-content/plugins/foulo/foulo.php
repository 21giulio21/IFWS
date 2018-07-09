<?php
/*
Plugin Name:  Foulo
Plugin URI:   https://goo.gl/maps/Gb6uzdDJWkS2
Description:  Per prendere fouli al porticciolo
Version:      21212121
Author:       Il Fuotografo
Author URI:   https://www.instagram.com/p/BeAZiVvjbEn/?taken-by=giulio_tavella
License:      GPL2
License URI:  https://www.gnu.org/licenses/gpl-2.0.html
*/

defined( 'ABSPATH' ) or die( 'No script kiddies please!' );

function login_func( $atts ){

  $result = "";

  if (session_status() == PHP_SESSION_NONE) {
    session_start();
  }

  if(
    isset($_SESSION["email"]) &&
    !empty($_SESSION["email"])
  ){
    $result .= '<h1>Ciao ' . $_SESSION["email"] . '</h1>';
    $result .= print_r($_SESSION, true);
  } else {
    $result .= '
      <form method="post">
        <input type="email" name="email" placeholder="Insert your email" value="" required/>
        <input type="password" name="password" value="" required />
        <input type="submit" name="submit" value="Login">
      </form>
    ';
  }
	return $result;
}

add_shortcode( 'login', 'login_func' );





function register_func( $atts ){

  $result = "";

  $result .= '
    <form method="post">
      <input type="email" name="register_email" placeholder="Insert your email" value="" required/>
      <input type="password" name="register_password" placeholder="Choose your password" value="" required />
      <input type="text" name="register_instagram_account" placeholder="Insert your Instagram account username" value="" required />
      <input type="submit" name="submit" value="Register">
    </form>
  ';

	return $result;
}

add_shortcode( 'register', 'register_func' );



function process_post() {

     // handling login process
     if( isset( $_POST['email'], $_POST['password'] ) ) {

       $target_url = "https://getfollowersoninstagram.altervista.org/app/checkUserIntoDatabase.php";
       $params =
        array(
          "email" => $_POST['email'],
          "password" => $_POST['password']
        );

       $curl_response = curl_request($target_url, $params);
       $parsed_response = json_decode($curl_response);

       if(isset($parsed_response->success) && $parsed_response->success == "success") {

         if (session_status() == PHP_SESSION_NONE) {
           session_start();
         }

         $_SESSION["email"] = $_POST['email'];

       }

     }

     // handling register process
     if( isset( $_POST['register_email'], $_POST['register_password'], $_POST['register_instagram_account'] ) ) {

       $target_url = "https://getfollowersoninstagram.altervista.org/app/insertUserIntoDatabase.php";
       $params =
        array(
          "email" => $_POST['register_email'],
          "password" => $_POST['register_password'],
          "username_instagram" => $_POST['register_instagram_account']
        );

       $curl_response = curl_request($target_url, $params);
       print_r($curl_response);

       $parsed_response = json_decode($curl_response);
       if(isset($parsed_response->success) && $parsed_response->success == "success") {

         if (session_status() == PHP_SESSION_NONE) {
           session_start();
         }

         $_SESSION["email"] = $_POST['email'];

       }

     }

}

add_action( 'init', 'process_post' );


function curl_request($target_url, array $arguments){

  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL,$target_url);
  curl_setopt($ch, CURLOPT_POST, 1);
  curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($arguments));

  // receive server response ...
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  $server_output = curl_exec ($ch);
  curl_close ($ch);
  return $server_output;

}

 ?>
