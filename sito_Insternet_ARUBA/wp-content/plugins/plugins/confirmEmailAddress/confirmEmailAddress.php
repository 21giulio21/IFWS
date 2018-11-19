<?php
/*
Plugin Name: Confirm Emai Address
Plugin URI:   https://goo.gl/mapfdgs/Gb6uregzdDJWkS2
Description:  Per confermare la mail
Version:      23243
Author:       Il Fu3
Author URI:   https://www.inew.com/p/Be32AZiVvjbEn/?taken-by=giulio_tavella
License:      GPL2
License URI:  https://www.gnu.org/licenses/gpl-2.0.html
*/
session_start();
require_once("instatrack_mail.php");

function sendMailToUser($codeMail)
{
  $to = $_SESSION["email"];
  $subject = "Instatrack.eu";
  $txt = getTextMail($codeMail);
  $headers = "From: verify@instatrack.eu\r\n";
  $headers .= "MIME-Version: 1.0\r\n";
  $headers .= "Content-Type: text/html; charset=ISO-8859-1\r\n";

  mail($to,$subject,$txt,$headers);


}

/*
Chiedo al server se la mail è gia occupata. In particolare la funziona tornando: $parsed_response->reason torna nulla se va tutto bene.
*/
function sendEmailAndPasswordToServerToRegisterUser($email,$password)
{
  $target_url = "http://2.230.243.113/instagram/app/register.php";
  $params =
   array(
     "EMAIL" => $email,
     "PASSWORD_SITE" => $password
   );

  $curl_response = curl_request($target_url, $params);
  $parsed_response = json_decode($curl_response);
  if (! is_null($parsed_response->reason))
  {
    return $parsed_response->reason;

  }



}

function confirmEmailAddress()
{

  $error = '';
  // se entro qui dentro allora entro perche ho premuto il pulsante dalla pagina corrente.
  if (isset($_POST["verification_code"]))
  {
    $code = $_SESSION["code"];
    $verification_code = $_POST["verification_code"];
    if($code == $verification_code)
    {

      $response = sendEmailAndPasswordToServerToRegisterUser($_SESSION["email"],$_SESSION["password"]);
      header('Location: http://www.instatrack.eu/dashboard');

      return;
    }else{
      $error = '<h3  style="color: red;" >Wrong verification code</h3>';

    }


  }

// se sono qui allora è la prima volta che ci arrivo e mando la mail.

//Prendo come input i parametri della pagina precedente e creo un codice da inserire che deve essere convalidato via mail.
$password =  $_SESSION["password"];
$email = $_SESSION["email"];
$codeMail = $_SESSION["code"];
// mando la mail all'utente con uqella mail.
sendMailToUser($codeMail);




// mostro un form con un semplice input text

$result = "";

$result .= '
       <div class="row">
         <div class="col-lg-4 col-lg-offset-4">';
         if (!is_null($error)) $result .=  '<h3  style="color: red;" >'.$error."</h3>";
         $result .='


         
           <form method="post">


             <div class="input-group">
               <span class="input-group-addon" style=" width: 44px; " ><i class="fa fa-envelope" aria-hidden="true"></i></span>
               <input type="text" name="verification_code" placeholder="Insert your validation code" value="" required/>
             </div>

              <br>

             <div class="form-group">
               <input type="submit" name="submit" value="Continue">
             </div>

           </form>
         </div>
       </div>
       ';
       return $result;




}

add_shortcode( 'confirmEmailAddress', 'confirmEmailAddress' );


?>
