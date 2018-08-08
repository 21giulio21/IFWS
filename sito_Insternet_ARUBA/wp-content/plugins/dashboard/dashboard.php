<?php
/*
Plugin Name:  Dashboard
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
session_start();


defined( 'ABSPATH' ) or die( 'No script kiddies please!' );


function dashboard_func( $atts ){

  wp_enqueue_script('foulo', plugin_dir_url(__FILE__) .'/js/foulo.js', array('jquery'), null, true);
  wp_enqueue_style( "foulocss", plugin_dir_url(__FILE__) .'/css/foulo.css');
  $result = "";

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

        <button type="button" id="button-rinnova" class="btn btn-default btn-lg">
          <span class="glyphicon glyphicon-plus" aria-hidden="true"></span> Update Subscription
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
           $instagram_user->COMMENTA . ',' .
           $instagram_user->DEVE_PAGARE . ',' .
           $instagram_user->TEMPO_FINE_ISCRIZIONE ;
    }


    if(!empty($instagram_linked_accounts))
      $result .= '
      <div class="row">
        <div class="col-lg-10">
          <div class="table-responsive account-list">
            <table class="table">
              <th>Instagram Account</th>
              <th>Bot status</th>
              <th>Activate/Deactivate Bot</th>
              <th>Activate/Deactivate Auuto-Comments</th>
              <th>Activate/Deactivate Auto-Like</th>
              <th>Subscription</th>
              <th>TARGET</th>
      ';
    foreach ($instagram_linked_accounts as $instagram_account )
    {
      $instagram_account_details = explode(",", $instagram_account);
      $bottoneAttiva = '';
      $bottoneDisattiva = '';
      $DEVE_PAGARE = $instagram_account_details[4];
      $secondi = $instagram_account_details[5];
      $testo = "";
      if($DEVE_PAGARE == "1")
      {

        // imposto il testo che vede essere NOT ACTIVE se non ha ancora pagato
        $testo = '<p style="color:red; font-size: 15px ">NOT ACTIVE</p>' ;

        //Se non ha ancora pagato quando premo il pulsante Active dovra aprire la view dove devo pagare
        $bottoneAttiva = '<button type="button" class="btn btn-danger" action="toggle-bot-pay" instagram-account="'.$instagram_account_details[0].'">
            Activate
        </button>';

      }
      else {
        //Ottengo la data per quanto ancora ha pagato e quindi copre l'abbonamento
        $date = date('Y-m-d', $secondi);
        $testo = '<p style="color:green; font-size: 15px">Active up to'.$date.' </p>' ;

        //ALtrimenti deve essere possibile attivare/Disattivare l'account
        $bottoneAttiva = '<button type="button" class="btn btn-danger" action="toggle-bot" instagram-account="'.$instagram_account_details[0].'">
            Activate
        </button>';
      }

      print_r($bottoneAttiva);


      $instagram_account_state = $instagram_account_details[1] == 1 ?
         '<i class="fa fa-check" aria-hidden="true"></i>' :
         '<i class="fa fa-times" aria-hidden="true"></i>';
      $instagram_account_state_button = $instagram_account_details[1] == 1 ?
         '<button type="button" class="btn btn-danger" action="toggle-bot" instagram-account="'.$instagram_account_details[0].'">
             Deactivate
         </button>' :
         $bottoneAttiva
         ;
      $instagram_comments_state = $instagram_account_details[3] == 1 ?
        '<button type="button" class="btn btn-danger" action="toggle-comments" instagram-account="'.$instagram_account_details[0].'">
            Deactivate
        </button>' :
        '<button type="button" class="btn btn-danger" action="toggle-comments" instagram-account="'.$instagram_account_details[0].'">
            Activate
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
              <button class="btn" action="toggle-likes" instagram-account="'.$instagram_account_details[0].'">
                  Deactivate
              </button>
            </td>

            <td>
            '.$testo.'
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

    //Devo tornare alla pagina precedente.
    //TODO
  }
	return $result;
}


add_shortcode( 'dashboard', 'dashboard_func' );



function getTargetFromDatabase()
{
  $target_url = "http://2.230.243.113/instagram/app/getCategory.php";
  $params = array();

  $curl_response = curl_request2($target_url, $params)or die("Non riesco a fare la curl");
  $parsed_response = json_decode($curl_response);
  $return_string = "";
  foreach ($parsed_response as $target) {
    $return_string = $return_string ."<option value=\"{$target->CATEGORY}\">{$target->CATEGORY}</option>";

  }

  return $return_string;
}






function process_post() {

     // handling login process
     if( isset( $_POST['email'], $_POST['password'] ) ) {
       $target_url = "http://2.230.243.113/instagram/app/login.php";
       $params =
        array(
          "EMAIL" => $_POST['email'],
          "PASSWORD_SITE" => $_POST['password']
        );

       $curl_response = curl_request2($target_url, $params)or die("Non riesco a fare la curl");
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

       $curl_response = curl_request2($target_url, $params);

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
          <input type="text" id="popup-username" class="form-control" placeholder="Username">
        </div>
        <div class="input-group">
          <span class="input-group-addon"><i class="fa fa-lock" aria-hidden="true"></i></span>
          <input type="password" id="popup-password" class="form-control" placeholder="Password">
        </div>
        <h3 id="errore-paragrafo" style="color: red;"  align="center" ></h3>
        <div id="box-loader" class="loader"></div>
        <br>
        <button id="new-account">Inserisci nuovo account</button>
      </div>
    </div>';
}
add_action( 'wp_footer', 'custom_code_footer_function' );

////////////////////MENU per il plus


function popup_pay() {

// Costruisco un menu a discesa dove ho tutti gli account

  $arrayUtentiInstagram = getInstagramProfilesFromEmail($_SESSION["email"]);
  $instagram_username = array();
  $instagram_TEMPO_FINE_ISCRIZIONE = array();
  $username_string = "";
  foreach ($arrayUtentiInstagram as $instagram_user) {
    $username_string = $username_string ."<option value=\"{$instagram_user->USERNAME}\">{$instagram_user->USERNAME}</option>";
    $instagram_username[] = $instagram_user->USERNAME;
    $instagram_TEMPO_FINE_ISCRIZIONE = $instagram_user->TEMPO_FINE_ISCRIZIONE;
  }

  if(!empty($instagram_username))
  {
    echo '
    <div id="popup-pay">
      <div>
        <div class="upper-bar">
          Renew your subscription
          <i class="fa fa-times" aria-hidden="true"></i>
        </div>
        <div class="input-group" align="center">
          Choose your account:
            <select>
              '.$username_string.'
            </select>
        </div>
        <div class="input-group" align="center" >
        Period:
            <button id="plus-button"><i class="fa fa-plus-square" aria-hidden="true"></i></button>&nbsp;
            <button id="minus-button"><i class="fa fa-minus"></i></button>&nbsp;
            <span id="tempo">0</span><span id="months"> Months</span>
        </div>
        <div class="input-group" align="center">
          <select id="box-plane" name="plane">
            <option value="1">Grow speed Medium - €19.99 per month </option>
            <option value="2">Grow speed Fast - €35.99 per month</option>
            <option value="3">Grow speed Turbo - €69.99 per month</option>
          </select>
          <div id="paypal-button"></div>
          <script src="https://www.paypalobjects.com/api/checkout.js"></script>
        </div>



      </div>
    </div>';
  }
}



add_action( 'wp_footer', 'popup_pay' );






////////////Fine



function curl_request2($target_url, array $arguments){

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

  $curl_response = curl_request2($target_url, $params);
  $parsed_response = json_decode($curl_response);
  return $parsed_response;

}

 ?>
