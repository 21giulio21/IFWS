<?php


require_once('../../util/connect.php');

/*
Questo file prende in input:
EMAIL
e controlla se la mail passata è nel database o meno, se è nel database alora torna 1

*/
if( !isset($_POST["EMAIL"]) || !isset($_POST["PASSWORD_SITE"]) )
{
  $return = '{ "success":"failed", "reason":"POST data not valid" }';
  echo $return;
  return;
}



$password_site = $_POST["PASSWORD_SITE"];
$email = $_POST["EMAIL"];


// Controllo che ci sia un utente con questa mail.
$query = "UPDATE `REGISTERED_USERS_FROM_WEBSITE` SET `PASSWORD_SITE` = ? WHERE `REGISTERED_USERS_FROM_WEBSITE`.`EMAIL` = ?;";
$stmt = $conn->prepare($query) or die("Errore nella prepare");
$stmt->bind_param("ss",$password_site,$email) or die("Errore nella bind_param");
$stmt->execute() or die("Errore nella execute");
echo "OK";




?>
