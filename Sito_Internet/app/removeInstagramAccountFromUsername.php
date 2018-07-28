<?php


require_once('../util/connect.php');

/*
Questo file permette di eliminare l'account Instagram collegato alla mail presa come input e username
*/
if( !isset($_POST["USERNAME"]))
{
  $return = '{ "success":"failed", "reason":"POST data not valid" }';
  echo $return;
  return;
}


$username = $_POST["USERNAME"];



$query = "DELETE FROM `REGISTERED_USERS` WHERE `REGISTERED_USERS`.`USERNAME` = ?";
$stmt = $conn->prepare($query)or die("Errore nella prepare");
$stmt->bind_param("s",$username)or die("Errore nella bind_param");
$stmt->execute()or die("Errore nella execute");


?>
