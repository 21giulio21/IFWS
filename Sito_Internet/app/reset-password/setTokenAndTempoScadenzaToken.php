<?php


require_once('../../util/connect.php');

/*
Questo file prende in input:
EMAIL
e controlla se la mail passata è nel database o meno, se è nel database alora torna 1

*/
if( !isset($_POST["EMAIL"]) || !isset($_POST["TEMPO_SCADENZA_TOKEN"]) || !isset($_POST["TOKEN"]) )
{
  $return = '{ "success":"failed", "reason":"POST data not valid" }';
  echo $return;
  return;
}




$email = $_POST["EMAIL"];
$tempo_scadenza_token = $_POST["TEMPO_SCADENZA_TOKEN"];
$token = $_POST["TOKEN"];


// Controllo che ci sia un utente con questa mail.
$query = "UPDATE `REGISTERED_USERS_FROM_WEBSITE` SET `TOKEN_RESET_PASSWORD` = ? ,
          `TEMPO_SCADENZA_TOKEN` = ? WHERE `REGISTERED_USERS_FROM_WEBSITE`.`EMAIL` = ?";
$stmt = $conn->prepare($query) or die("Errore nella prepare");
$stmt->bind_param("sss",$token,$tempo_scadenza_token,$email) or die("Errore nella bind_param");
$stmt->execute() or die("Errore nella execute");

$return = '{ "success":"success" }';

echo $return;




?>
