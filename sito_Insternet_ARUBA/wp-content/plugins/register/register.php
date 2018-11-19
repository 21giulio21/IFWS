<?php
   /*
   Plugin Name: Register
   Plugin URI:   https://goo.gl/maps/Gb6uzdDJWkS2
   Description:  Per prendere fouli al porticciolo
   Version:      21212121
   Author:       Il Fuotografo
   Author URI:   https://www.instagram.com/p/BeAZiVvjbEn/?taken-by=giulio_tavella
   License:      GPL2
   License URI:  https://www.gnu.org/licenses/gpl-2.0.html
   */

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

/*
Chiedo al server se la mail è gia occupata. In particolare la funziona tornando: $parsed_response->reason torna nulla se va tutto bene.
*/
function checkIfEmailIsOccupate($email)
{
  $target_url = "http://www.elenarosina.com/instatrack/app/checkIfEmailIsOccupate.php";
  $params =
   array(
     "EMAIL" => $email
   );

  $curl_response = curl_request($target_url, $params);
  $parsed_response = json_decode($curl_response);
  if (! is_null($parsed_response->reason))
  {
    return $parsed_response->reason;

  }



}

//Funzione che controlla che la mail inserita è una mail o meno.
function checkEmail2($email) {
   if ( strpos($email, '@') !== false ) {
      $split = explode('@', $email);
      return (strpos($split['1'], '.') !== false ? true : false);
   }
   else {
      return false;
   }
}


//////////////////////
function post_captcha($user_response) {
    $fields_string = '';
    $fields = array(
        'secret' => '6LcnSGgUAAAAAIBIJjG9JLa-WV_q7mg3f-r0tshZ',
        'response' => $user_response
    );
    foreach($fields as $key=>$value)
    $fields_string .= $key . '=' . $value . '&';
    $fields_string = rtrim($fields_string, '&');

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, 'https://www.google.com/recaptcha/api/siteverify');
    curl_setopt($ch, CURLOPT_POST, count($fields));
    curl_setopt($ch, CURLOPT_POSTFIELDS, $fields_string);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, True);

    $result = curl_exec($ch);
    curl_close($ch);


    return json_decode($result, true);
}

/*
COntrollo che mi siano arrivate le credenziali inserite. Questa pagina manda le credenziali a se stessa, le controlla e poi,
se va tutto
*/
function parseDataFromPost2()
{

  // controllo siano settati la mail e la password.
  if( isset($_POST["register_email"]) && isset($_POST["register_password"]) )
  {
    // controllo che il coso robot sia ok
    $res = post_captcha($_POST['g-recaptcha-response']);

    //Se non ho inserito il coso robot lo scrivo
    if (!$res['success']) {
      return 'Please make sure you check the security CAPTCHA box.';

    }


    $email = $_POST["register_email"];
    $password = $_POST["register_password"];

    //Controllo che la mail sia veramente una mail
    if (!checkEmail2($email))
    {
      return 'Indirizzo email non valido';

    }

    //Controllo che la password sia almeno lunga 8 caratteri
    if(strlen($password) < 8)
    {
      return 'La password deve contenere almeno 8 caratteri';

    }

    //Faccio una query al database per vedere se c'è un itente con quella mail, se non risponde nulla allora va bene e proseguo
    $return = checkIfEmailIsOccupate($email);
    if(!is_null($return))
    {
      return $return;
    }
    // se sono qui allora devo andare alla pagina di conferma indirizzo email.

    /*
    Precedentemente si mandava la mail di conferma ora non la mando per questioni di velocità nella registrazione.
    Quindi se si vuole mandare la mail il codice per mandarla è questo qui sotto. basta togliere i commenti

    // ora mi sposto nella pagina confirmEmailAddress per poter verificare la mail.
    $_SESSION["password"] = $password;
    $_SESSION["email"] = $email;
    $_SESSION["code"]= rand(10000,99999);
    header('Location: http://www.instatrack.eu/confirmEmailAddress');
    */

    $_SESSION["password"] = $password;
    $_SESSION["email"] = $email;
    $response = sendUsernameAndPasswordToServerToRegisterUser($_SESSION["email"],$_SESSION["password"]);
    header('Location: http://www.instatrack.eu/dashboard');

  }
}
function sendUsernameAndPasswordToServerToRegisterUser($email,$password)
{
  $target_url = "http://www.elenarosina.com/instatrack/app/register.php";
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

function register_func( $atts ){

  wp_enqueue_script('foulo', plugin_dir_url(__FILE__) .'register.js', array('jquery'), null, true);

  //Se response non è nullo lo stampo in rosso sopra al form
  $response = parseDataFromPost2();



     $result = "";

     $result .= '
     <div class="row">
       <div class="col-lg-4 col-lg-offset-4">';
       if (!is_null($response)) $result .=  '<h3  style="color: red;" >'.$response."</h3>";
       $result .='

       <h3>Create an Instatrack account</h3>

         <form method="post">


           <div class="input-group">
             <span class="input-group-addon" style=" width: 44px; " ><i class="fa fa-envelope" aria-hidden="true"></i></span>
             <input type="email" name="register_email" placeholder="Inserisci la tua email" value="" required/>
           </div>
<br>

           <div class="input-group">
             <span class="input-group-addon" style=" width: 44px; " ><i class="fa fa-lock" aria-hidden="true"></i></span>
              <input type="password" name="register_password" placeholder="Scegli una password" value="" required />
           </div>


           <div class="form-group">
             <br><div class="g-recaptcha" data-sitekey="6LcnSGgUAAAAAF3pZ9cr8-1rZeGivwOydDhEgNdo"></div>
<br>
             <input type="submit" name="submit" value="Registrati">
           </div>
         </form>
       </div>
     </div>
     ';

   	return $result;
   }

   add_shortcode( 'register', 'register_func' );
?>
