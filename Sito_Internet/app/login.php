<?php


require_once('../util/connect.php');

/*
Questo file prende in input:
EMAIL
PASSWORD_SITE

e controllo che questo utente sia gia nel database, se è nel database restituisco un json
con scritto success.

*/
$email_user = $_POST["EMAIL"];
$password_site = $_POST["PASSWORD_SITE"];

// Controllo che ci sia un utente con queste credenziali.
$query = "SELECT * FROM `REGISTERED_USERS` WHERE `EMAIL` = ? AND `PASSWORD_SITE` = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("ss",$email_user,$password_site);
$stmt->execute();
$stmt->store_result();

if ($stmt->num_rows == 1 )
{
//Se sono qui allora ritorno che ho unutente con quelle credenziali
$return = '{ "success":"success" }';

echo $return;

}else{

  $return = '{ "success":"failed", "reason":"Credentials not valid" }';
  echo $return;


}




?>
