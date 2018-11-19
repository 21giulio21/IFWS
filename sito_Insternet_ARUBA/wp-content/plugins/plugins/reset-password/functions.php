<?php
require_once("reset_password_mail.php");
function curl_custom($target_url, array $arguments){

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

function post_captcha5($user_response) {
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
function checkIfInputIsEmail($email) {
   if ( strpos($email, '@') !== false ) {
      $split = explode('@', $email);
      return (strpos($split['1'], '.') !== false ? true : false);
   }
   else {
      return false;
   }
}

//Funzione che prende in argomento la mail e controlla se è gia presa o meno.
// Se la funzione non risponde nulla allora è funzionato benissimo!
function checkIfEmailIsIntoDatabase($email)
{
  $target_url = "http://2.230.243.113/instagram/app/reset-password/checkIfEmailIsIntoDatabase.php";
  $params =
   array(
     "EMAIL" => $email
   );

  $curl_response = curl_custom($target_url, $params);
  $parsed_response = json_decode($curl_response);
  if (!is_null($parsed_response->reason))
  {
    return $parsed_response->reason;

  }


}
function sendTokenAndTempoScadenzaTokenToServer($email,$token,$tempo_scadenza_token)
{
  $target_url = "http://2.230.243.113/instagram/app/reset-password/setTokenAndTempoScadenzaToken.php";
  $params =
   array(
     "EMAIL" => $email,
     "TOKEN" => $token,
     "TEMPO_SCADENZA_TOKEN" => $tempo_scadenza_token
   );

  $curl_response = curl_custom($target_url, $params);
  print($curl_response);

}

function sendTokenMailToUser($text,$email)
{
  $to = $_SESSION["email"];

  $subject = "Instatrack.eu";
  $txt = getMaiResetPasswordlText($text);
  $headers = "From: verify@instatrack.eu\r\n";
  $headers .= "MIME-Version: 1.0\r\n";
  $headers .= "Content-Type: text/html; charset=ISO-8859-1\r\n";

  mail($email,$subject,$txt,$headers);


}

function getTokenFromDatabaseFromEmail($email,$token)
{
  $target_url = "http://2.230.243.113/instagram/app/reset-password/getTokenFromEmail.php";
  $params =
   array(
     "EMAIL" => $email,
     "TOKEN" =>$token
   );

  $curl_response = curl_custom($target_url, $params);
  return $curl_response;
}

function sendToDatabaseNewPassword($email,$password)
{
    
  $target_url = "http://2.230.243.113/instagram/app/reset-password/setPasswordIntoDatabase.php";
  $params =
   array(
     "EMAIL" => $email,
     "PASSWORD_SITE" =>$password
   );

  $curl_response = curl_custom($target_url, $params);
  echo $curl_response;
  return $curl_response;

}




?>
