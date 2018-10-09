<?php
require_once('../util/connect.php');

/*
Questo file permette di inserire nel database un nuovvo messaggio che deve essere mandato ad utente.
Il NUMERO_TELEFONICO non deve contenere il +39 ma 0039
*/

if( !isset($_GET["EMAIL"])|| !isset($_GET["MESSAGGIO"]) || !isset($_GET["OGGETTO"])  )
{
  $return = '{ "success":"failed", "reason":"GET data not valid" }';
  echo $return;
  return;
}


$email = $_GET["EMAIL"];
$messaggio = $_GET["MESSAGGIO"];
$oggetto = $_GET["OGGETTO"];


$query = "INSERT INTO `MAIL_INSTATRACK` (`ID`, `EMAIL`, `MESSAGGIO`, `OGGETTO`) VALUES (NULL, ?, ?, ?);";
$stmt = $conn->prepare($query)or die("Errore nella prepare");
$stmt->bind_param("sss",$email,$messaggio,$oggetto)or die("Errore nella bind_param");
$stmt->execute()or die("Errore nella execute");


?>
