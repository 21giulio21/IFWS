<?php

/*
Plugin Name: Login
Plugin URI:   https://goo.gl/mapfdgs/Gb6uzdDJWkS2
Description:  Per prendedfgre fouli al porticciolo
Version:      2324
Author:       Il Fuotografo32
Author URI:   https://www.inew.com/p/BeAZiVvjbEn/?taken-by=giulio_tavella
License:      GPL2
License URI:  https://www.gnu.org/licenses/gpl-2.0.html
*/

   function curl_request5($target_url, array $arguments){

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

//Funzione che prende in argomento la mail e controlla se è gia presa o meno.
// Se la funzione non risponde nulla allora è funzionato benissimo!
function sendCredentialsToServer2($email,$password)
{
  $target_url = "http://2.230.243.113/instagram/app/login.php";
  $params =
   array(
     "EMAIL" => $email,
     "PASSWORD_SITE" => $password

   );

  $curl_response = curl_request5($target_url, $params);
  $parsed_response = json_decode($curl_response);
  if (! is_null($parsed_response->reason))
  {
    return $parsed_response->reason;

  }


}

function post_captcha2($user_response) {
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


//Funzione che controlla che la mail inserita è una mail o meno.
function checkEmail($email) {
   if ( strpos($email, '@') !== false ) {
      $split = explode('@', $email);
      return (strpos($split['1'], '.') !== false ? true : false);
   }
   else {
      return false;
   }
}



/*
COntrollo che mi siano arrivate le credenziali inserite. Questa pagina manda le credenziali a se stessa, le controlla e poi,
se va tutto
*/
function parseDataPost()
{

  if( isset($_POST["register_email"]) && isset($_POST["register_password"]) )
  {
    // controllo che il coso robot sia ok
    $res = post_captcha($_POST['g-recaptcha-response']);

    //Se non ho inserito il coso robot lo scrivo
    if (!$res['success']) {
      return 'Please make sure you check the security CAPTCHA box.';

    }
  }

  if( isset($_POST["register_email"]) && isset($_POST["register_password"]) )
  {
    $email = $_POST["register_email"];
    $password = $_POST["register_password"];

    //Controllo che la mail sia corretta.
    if (!checkEmail($email))
    {
      return 'Enter a valid email address';

    }

    //Mando i dati al server che controlla in utomatico se sono gia inserite credenziali ugiali o altro,
    //Devo solo fare un pars della risposta.
    $response = sendCredentialsToServer2($email,$password);

  // se response è null allora è funzionato bene tutto, altrimenti stampo nella parte sopra del form la response
    if (is_null($response))
    {

      session_start();

      $_SESSION["email"] = $email;

      // Mi sposto sulla pagina della dashboard
      header('Location: http://www.instatrack.eu/dashboard');
      return;

    }else{
      return $response;
    }
  }
}


function login_func( ){

  wp_enqueue_script('foulo', plugin_dir_url(__FILE__) .'login.js', array('jquery'), null, true);


  //Se response non è nullo lo stampo in rosso sopra al form
    $response = parseDataPost();



       $result = "";

       $result .= '
       <div class="row">
         <div class="col-lg-4 col-lg-offset-4">';
         if (!is_null($response)) $result .= '<h3  style="color: red;" >'.$response."</h3>";
         $result .='


         <h3>Log in to Instatrack</h3>
           <form method="post">


             <div class="input-group">
               <span class="input-group-addon" style=" width: 44px; " ><i class="fa fa-envelope" aria-hidden="true"></i></span>
               <input type="email" name="register_email" placeholder="Insert your email" value="" required/>
             </div>

              <br>

             <div class="input-group">
               <span class="input-group-addon" style=" width: 44px; " ><i class="fa fa-lock" aria-hidden="true"></i></span>
                <input type="password" name="register_password" placeholder="Insert your password" value="" required />
             </div>

             <br>

             <div class="form-group">
               <br><div class="g-recaptcha" data-sitekey="6LcnSGgUAAAAAF3pZ9cr8-1rZeGivwOydDhEgNdo"></div><br>


              <span>Forgot your password?  <a href="http://www.instatrack.eu/reset-password/">Click here</a></span><br><br>
               <span>New to Instatrack?  <a href="https://www.instatrack.eu/register">Create an account now.</a></span><br><br>

               <input type="submit" name="submit" value="Login">
             </div>
           </form>
         </div>
       </div>
       ';

     	return $result;
}


add_shortcode( 'login', 'login_func' );


?>
