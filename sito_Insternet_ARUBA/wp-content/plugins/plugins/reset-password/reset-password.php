<?php

/*
Plugin Name:  Reset Password
Plugin URI:   https://goo.gl/mapfdeegs/Gb6uzdDJWkS2
Description:  Per prendedfgre foeeuli al porticciolo
Version:      232432
Author:       Il ew
Author URI:   https://www.inew.ewcom/p/3BeAZi3VvjbEn/?taken-by=giulio_tavella
License:      GPL2
License URI:  https://www.gnu.org/licenses/gpl-2.0.html
*/
require_once("functions.php");
session_start();


/*
COntrollo che mi siano arrivate le credenziali inserite. Questa pagina manda le credenziali a se stessa, le controlla e poi,
se va tutto
*/
function parseDataPost3()
{

  if( isset($_POST["reset_password"]) )
  {
    echo "FFFF ".$_POST["reset_password"];
    if(strlen($_POST["reset_password"])<7)
    {
      return "The password must contain at least 8 characters";
    }

    echo "email_reset_password ".$_SESSION["email_reset_password"];
    echo "reset_password ".$_POST["reset_password"];

    $response = sendToDatabaseNewPassword($_SESSION["email_reset_password"],$_POST["reset_password"]);
    if($response == "OK")
    {
      header('Location: http://www.instatrack.eu/e-mail-changed-successfully/');


    }
  }


  if( isset($_POST["reset_email"]) )
  {
    // controllo che il coso robot sia ok
    $res = post_captcha($_POST['g-recaptcha-response']);

    //Se non ho inserito il coso robot lo scrivo
    if (!$res['success']) {
      return 'Please make sure you check the security CAPTCHA box.';

    }

    $email = $_POST["reset_email"];

    //Controllo che la mail sia corretta.
    if (!checkIfInputIsEmail($email))
    {
      return 'Enter a valid email address';

    }


    //Mando i dati al server che controlla in utomatico se sono gia inserite credenziali ugiali o altro,
    //Devo solo fare un pars della risposta.
    $response = checkIfEmailIsIntoDatabase($email);

  // se response è null allora è funzionato bene tutto, altrimenti stampo nella parte sopra del form la response
    if (is_null($response))
    {

      $token = md5(uniqid(rand(), true));
      // imposto che il token scade 1 ora dopo avelo inserito.
      $tempo_scadenza_token = time() + 3600;
      sendTokenAndTempoScadenzaTokenToServer($email,$token,$tempo_scadenza_token);
      $text = '<a href= "https://www.instatrack.eu/enter-new-password/?email='.$email.'&token='.$token.'" >https://www.instatrack.eu/enter-new-password/?email='.$email.'&token='.$token.'</a>';
      sendTokenMailToUser($text,$email);
      header('Location: https://www.instatrack.eu/wait-mail/');

    }else{
      return $response;
    }

  }
}

add_shortcode( 'reset-password', 'reset_password_function' );
function reset_password_function( ){

  wp_enqueue_script('foulo', plugin_dir_url(__FILE__) .'reset-password.js', array('jquery'), null, true);


  //Se response non è nullo lo stampo in rosso sopra al form
    $response = parseDataPost3();



       $result = "";

       $result .= '
       <div class="row">
         <div class="col-lg-4 col-lg-offset-4">';
         if (!is_null($response)) $result .= '<h3  style="color: red;" >'.$response."</h3>";
         $result .='


         <h3>Reset your password</h3>
         <p>To reset your password, enter the email address you use to sign in into instatrack.eu</p>
           <form method="post">


             <div class="input-group">
               <span class="input-group-addon" style=" width: 44px; " ><i class="fa fa-envelope" aria-hidden="true"></i></span>
               <input type="email" name="reset_email" placeholder="Insert your email" value="" required/>
             </div>

              <br>

             <br>

             <div class="form-group">
               <br><div class="g-recaptcha" data-sitekey="6LcnSGgUAAAAAF3pZ9cr8-1rZeGivwOydDhEgNdo"></div><br>
               <input type="submit" name="submit" value="Get Reset Link">
             </div>
           </form>
         </div>
       </div>
       ';

     	return $result;
}
add_shortcode("enter_new_password","enter_new_password");
function enter_new_password(){
  parseDataPost3();
  $t = "";



  // Controllo per prima cosa che siano settati tutti i parametri mandati per mail:
  // 1) Token
  // 2) email
  if(!isset($_GET["email"]) || !isset($_GET["token"]) )
  {
    $t .='Corrupt link';
    return $t;

  }
  $email = $_GET["email"];
  $token = $_GET["token"];
  $_SESSION["email_reset_password"] =   $email;

  //Ottengo il token presente nel database dell'utente che ha vhiesto il recupero password.
  $response = getTokenFromDatabaseFromEmail($email,$token);
  if($response == 1)
  {
    //Faccio un form per l'inserimento della nuova password.
    $t .= '
    <div class="row">
      <div class="col-lg-4 col-lg-offset-4">


      <h3>Insert a new password</h3>
      <p>The password must contain at least 8 characters</p>
        <form method="post">


          <div class="input-group">
            <span class="input-group-addon" style=" width: 44px; " ><i class="fa fa-lock" aria-hidden="true"></i></span>
            <input type="password" name="reset_password" placeholder="Insert your new password" value="" required/>
          </div>

           <br>

          <br>

          <div class="form-group">
            <br><div class="g-recaptcha" data-sitekey="6LcnSGgUAAAAAF3pZ9cr8-1rZeGivwOydDhEgNdo"></div><br>
            <input type="submit" name="submit" value="Get Reset Link">
          </div>
        </form>
      </div>
    </div>
    ';

  }

  return $t;



}







?>
