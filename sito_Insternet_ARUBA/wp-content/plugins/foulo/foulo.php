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
    $result .= print_r($_SESSION, true) . "<br/>";
    if(!empty($_SESSION["instagram_linked_accounts"]))
      $result .= '
      <div class="row">
        <div class="col-lg-9">
          <div class="table-responsive account-list">
            <table class="table">
              <th>Account Instagram</th>
              <th>Stato Bot</th>
              <th>Azione</th>
      ';
    foreach ($_SESSION["instagram_linked_accounts"] as $instagram_account ) {
      $result .= '
          <tr>
            <td>
              <a href="https://www.instagram.com/'.$instagram_account.'" target="_blank">
                @'.$instagram_account.'
              </a>
            </td>
            <td>
              <p>attivo</p>
            </td>
            <td>
              <button class="btn btn-danger" instagram-account="'.$instagram_account.'">
                  Disattiva
              </button>
            </td>
          </tr>
      ';
    }
    if(!empty($_SESSION["instagram_linked_accounts"]))
      $result .= '
            </table>
          </div>
        </div>
      ';
  } else {
    $result .= '
      <div class="row">
        <div class="col-lg-4 col-lg-offset-4">
          <form method="post">
            <div class="form-group">
              <input type="text" class="form-control" name="email" placeholder="Insert your email" value="" required/>
            </div>
            <div class="form-group">
              <input type="password" class="form-control" name="password" placeholder="Insert your password" value="" required />
            </div>
            <div class="form-group">
              <input type="submit" name="submit" value="Login">
            </div>
          </form>
        </div>
      </div>
    ';
  }
	return $result;
}

add_shortcode( 'login', 'login_func' );





function register_func( $atts ){

  $result = "";

  $result .= '
    <form method="post">
      <input type="text" name="register_email" placeholder="Insert your email" value="" required/>
      <input type="text" name="register_password" placeholder="Choose your password" value="" required />
      <input type="text" name="register_confirm_password" placeholder="Confirm password" value="" required />
      <input type="submit" name="submit" value="Register">
    </form>
  ';

	return $result;
}

add_shortcode( 'register', 'register_func' );



function process_post() {

     // handling login process
     if( isset( $_POST['email'], $_POST['password'] ) ) {
       $target_url = "http://2.230.243.113/instagram/app/login.php";
       $params =
        array(
          "EMAIL" => $_POST['email'],
          "PASSWORD_SITE" => $_POST['password']
        );

       $curl_response = curl_request($target_url, $params)or die("Non riesco a fare la curl");
       $parsed_response = json_decode($curl_response);

       if(isset($parsed_response->success) && $parsed_response->success == "success") {

         if (session_status() == PHP_SESSION_NONE) {
           session_start();
         }

         $arrayUtentiInstagram = getInstagramProfilesFromEmail($email);
         print_r($arrayUtentiInstagram);
         $instagram_linked_accounts = array();

         foreach ($arrayUtentiInstagram as $instagram_user) {
             $instagram_linked_accounts[] = $instagram_user->USERNAME . "," .
                $instagram_user->SCRIPT_ACTIVE . "," . $instagram_user->PASSWORD_ERRATA;
         }


         $_SESSION["email"] = $_POST['email'];
         $_SESSION["instagram_linked_accounts"] = $instagram_linked_accounts;

       }

     }

     // handling register process
     if( isset( $_POST['register_email'], $_POST['register_password'], $_POST['register_confirm_password'] ) ) {

       $target_url = "http://2.230.243.113/instagram/app/register.php";
       $params =
        array(
          "EMAIL" => $_POST['register_email'],
          "PASSWORD_SITE" => $_POST['register_password']
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

}

add_action( 'init', 'process_post' );


function curl_request($target_url, array $arguments){

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

function getInstagramProfilesFromEmail(){
  $target_url = "http://2.230.243.113/instagram/app/getInstagramProfilesFromEmail.php";
  $params =
   array(
     "EMAIL" => $_POST['email']
   );

  $curl_response = curl_request($target_url, $params);
  $parsed_response = json_decode($curl_response);
  return $parsed_response;

}

 ?>
