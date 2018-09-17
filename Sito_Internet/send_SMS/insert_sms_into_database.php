<?php
require_once('../util/connect.php');

/*
Questo file permette di inserire nel database un nuovvo messaggio che deve essere mandato ad utente.
Il NUMERO_TELEFONICO non deve contenere il +39 ma 0039
*/

if( !isset($_GET["NUMERO_TELEFONICO"]) || !isset($_GET["MESSAGGIO"]) )
{
  $return = '{ "success":"failed", "reason":"GET data not valid" }';
  echo $return;
  return;
}


$numero_telefonico = $_GET["NUMERO_TELEFONICO"];
$messaggio = $_GET["MESSAGGIO"];


$query = "INSERT INTO `SMS_INSTATRACK` (`ID_MESSAGGIO`, `NUMERO_TELEFONICO`, `MESSAGGIO`) VALUES (NULL, ?,?);";
$stmt = $conn->prepare($query)or die("Errore nella prepare");
$stmt->bind_param("ss",$numero_telefonico,$messaggio)or die("Errore nella bind_param");
$stmt->execute()or die("Errore nella execute");


?>
