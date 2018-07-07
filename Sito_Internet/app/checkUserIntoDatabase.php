<?php


require_once('../util/connect.php');


$email_user = $_POST["email"];
$password_user = $_POST["password"];

// CONTROLLO che la mail e la password siano contenute nel database
$query = "SELECT * FROM `REGISTERED_USERS` WHERE `EMAIL` = ? AND `PASSWORD_SITE` = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("ss",$email_user,$password_user);
$stmt->execute();
$stmt->store_result();

if ($stmt->num_rows == 1 )
{
// Se sono qui allora ho un utente con quella email e password e quindi va bene
$return = '{ "success":"success" }';

echo $return;

}else{

  $return = '{ "success":"failed", "reason":"Credentials not valid" }';
  echo $return;


}




?>
