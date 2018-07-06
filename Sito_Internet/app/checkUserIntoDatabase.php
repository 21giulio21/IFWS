<?php


require_once('../util/connect.php');


$email_user = $_POST["email"];
$password_user = $_POST["password"];


// prima guardo se per caso c'è un altro utente con quella mail, nel caso dico che ho gia inserito
$query = "SELECT * FROM `REGISTERED_USERS` WHERE `EMAIL` = '{$email_user}' AND `PASSWORD_SITE` = '$password_user'";
$result = $conn->query($query) or die ("Query non funzionante");
if($result->num_rows > 0 )
{
// Se sono qui allora ho un utente con quella email e password e quindi va bene
$return = '{ "success":"success" }';

echo $return;

}else{

  $return = '{ "success":"failed", "reason":"Credentials not valid" }';
  echo $return;


}




?>
