<?php


require_once('../../util/connect.php');

/*
Questo file prende in input:
EMAIL
e controlla se la mail passata è nel database o meno, se è nel database alora torna 1

*/
if( !isset($_POST["EMAIL"]) ||  !isset($_POST["TOKEN"])  )
{
  $return = '{ "success":"failed", "reason":"POST data not valid" }';
  echo $return;
  return;
}
$token = $_POST["TOKEN"];
$email = $_POST["EMAIL"];


// Controllo che ci sia un utente con questa mail.
$query = "SELECT * FROM `REGISTERED_USERS_FROM_WEBSITE` WHERE `EMAIL` = ? AND `TOKEN_RESET_PASSWORD` = ? ";
$stmt = $conn->prepare($query) or die("Errore nella prepare");
$stmt->bind_param("ss",$email,$token) or die("Errore nella bind_param");
$stmt->execute() or die("Errore nella execute");
$stmt->store_result() or die("Errore nella prepare");

if ($stmt->num_rows == 1 )
{
//Se sono qui allora ritorno che ho unutente con quelle credenziali
$return = "1";

echo $return;

}else{

  $return ="0";
  echo $return;


}




?>
