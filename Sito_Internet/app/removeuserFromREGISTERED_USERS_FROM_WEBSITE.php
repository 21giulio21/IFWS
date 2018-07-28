<?php


require_once('../util/connect.php');

/*
Questo file permette di eliminare l'account isnerito dal sito.
Elimino l'account dal database REGISTERED_USERS_FROM_WEBSITE
*/


if( !isset($_POST["EMAIL"]))
{
  $return = '{ "success":"failed", "reason":"POST data not valid" }';
  echo $return;
  return;
}


$email = $_POST["EMAIL"];



$query = "DELETE FROM `REGISTERED_USERS_FROM_WEBSITE` WHERE `REGISTERED_USERS_FROM_WEBSITE`.`EMAIL` = ?";
$stmt = $conn->prepare($query)or die("Errore nella prepare");
$stmt->bind_param("s",$email)or die("Errore nella bind_param");
$stmt->execute()or die("Errore nella execute");


?>
