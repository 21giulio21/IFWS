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

//Includo il file login.php perchè contiene la funzione di login,
// non è in questo file la funzione di login per ordine.
require_once("login.php");

defined( 'ABSPATH' ) or die( 'No script kiddies please!' );

function login_func( $atts ){
  wp_enqueue_script('foulo', plugin_dir_url(__FILE__) .'/js/foulo.js', array('jquery'), null, true);
  wp_enqueue_style( "foulocss", plugin_dir_url(__FILE__) .'/css/foulo.css');
  $result = "";

  if (session_status() == PHP_SESSION_NONE) {
    session_start();
  }

  if(
    isset($_SESSION["email"]) &&
    !empty($_SESSION["email"])
  ){
    $result .= '
      <div class="row" style="margin-bottom:30px;">
        <div class="col-lg-10">
          <h1 style="margin:0">Ciao ' . $_SESSION["email"] . '</h1>
        </div>
        <div class="col-lg-2">
        <button type="button" id="toggle-account-box" class="btn btn-default btn-lg">
          <span class="glyphicon glyphicon-plus" aria-hidden="true"></span> Aggiungi account
        </button>
        </div>
      </div>
    ';
    $category = getTargetFromDatabase();
    $arrayUtentiInstagram = getInstagramProfilesFromEmail($_SESSION["email"]);

    $instagram_linked_accounts = array();

    foreach ($arrayUtentiInstagram as $instagram_user) {
        $instagram_linked_accounts[] = $instagram_user->USERNAME . "," .
           $instagram_user->SCRIPT_ACTIVE . "," .
           $instagram_user->PASSWORD_ERRATA . ',' .
           $instagram_user->COMMENTA
           ;
    }

    if(!empty($instagram_linked_accounts))
      $result .= '
      <div class="row">
        <div class="col-lg-10">
          <div class="table-responsive account-list">
            <table class="table">
              <th>Account Instagram</th>
              <th>Stato Bot</th>
              <th>Attiva/Disattiva Bot</th>
              <th>Attiva/Disattiva Commenti</th>
              <th>Attiva/Disattiva Like</th>
              <th>TARGET</th>
      ';
    foreach ($instagram_linked_accounts as $instagram_account ) {
      $instagram_account_details = explode(",", $instagram_account);
      $instagram_account_state = $instagram_account_details[1] == 1 ?
         '<i class="fa fa-check" aria-hidden="true"></i>' :
         '<i class="fa fa-times" aria-hidden="true"></i>';
      $instagram_account_state_button = $instagram_account_details[1] == 1 ?
         '<button type="button" class="btn btn-danger" action="toggle-bot" instagram-account="'.$instagram_account_details[0].'">
             Disattiva
         </button>' :
         '<button type="button" class="btn btn-danger" action="toggle-bot" instagram-account="'.$instagram_account_details[0].'">
             Attiva
         </button>'
         ;
      $instagram_comments_state = $instagram_account_details[3] == 1 ?
        '<button type="button" class="btn btn-danger" action="toggle-comments" instagram-account="'.$instagram_account_details[0].'">
            Disattiva
        </button>' :
        '<button type="button" class="btn btn-danger" action="toggle-comments" instagram-account="'.$instagram_account_details[0].'">
            Attiva
        </button>';
      $result .= '
          <tr>
            <td>
              <a href="https://www.instagram.com/'.$instagram_account_details[0].'" target="_blank">
                @'.$instagram_account_details[0].'
              </a>
            </td>
            <td>
              <p>' . $instagram_account_state .'</p>
            </td>
            <td>
              '.$instagram_account_state_button .'
            </td>
            <td>
              '.$instagram_comments_state.'
            </td>
            <td>
              <button class="btn disabled" action="toggle-likes" instagram-account="'.$instagram_account_details[0].'">
                  Disattiva
              </button>
            </td>

            <td>
              <select>
                '.$category.'
              </select>
            </td>


          </tr>
      ';
    }
    if(!empty($instagram_linked_accounts))
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

function getTargetFromDatabase()
{
  $target_url = "http://2.230.243.113/instagram/app/getCategory.php";
  $params = array();

  $curl_response = curl_request($target_url, $params)or die("Non riesco a fare la curl");
  $parsed_response = json_decode($curl_response);
  $return_string = "";
  foreach ($parsed_response as $target) {
    $return_string = $return_string ."<option value=\"{$target->CATEGORY}\">{$target->CATEGORY}</option>";

  }

  return $return_string;
}



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

         $_SESSION["email"] = $_POST['email'];

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

function custom_code_footer_function() {
    echo '
    <div id="new-account-box">
      <div>
        <div class="upper-bar">
          Aggiungi un nuovo account Instagram
          <i class="fa fa-times" aria-hidden="true"></i>
        </div>
        <div class="input-group">
          <span class="input-group-addon"><i class="fa fa-at" aria-hidden="true"></i></span>
          <input type="text" class="form-control" placeholder="Username">
        </div>
        <div class="input-group">
          <span class="input-group-addon"><i class="fa fa-lock" aria-hidden="true"></i></span>
          <input type="password" id="account-password" class="form-control" placeholder="Password">
        </div>
        <button id="new-account">Inserisci nuovo account</button>
      </div>
    </div>';
}
add_action( 'wp_footer', 'custom_code_footer_function' );


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

function getInstagramProfilesFromEmail($email){
  $target_url = "http://2.230.243.113/instagram/app/getInstagramProfilesFromEmail.php";
  $params =
   array(
     "EMAIL" => $email
   );

  $curl_response = curl_request($target_url, $params);
  $parsed_response = json_decode($curl_response);
  return $parsed_response;

}

 ?>
