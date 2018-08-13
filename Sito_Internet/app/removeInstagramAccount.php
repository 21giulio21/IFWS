<?php
require_once('../util/connect.php');

if( !isset($_POST["username"]) )
{
  $return = '{ "success":"failed", "reason":"POST data not valid" }';
  echo $return;
  return;
}

$username = $_POST["username"];

echo "Rimuovo" .$username;

$query = "DELETE FROM `REGISTERED_USERS` WHERE `REGISTERED_USERS`.`USERNAME` = ? ";
$stmt = $conn->prepare($query)or die("Errore nella prepare");
$stmt->bind_param("s",$username)or die("Errore nella bind_param");
$stmt->execute()or die("Errore nella execute");

?>
