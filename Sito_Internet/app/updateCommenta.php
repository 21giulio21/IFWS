<?php


require_once('../util/connect.php');


if( !isset($_POST["username"]) || !isset($_POST["commenta"]) )
{
  $return = '{ "success":"failed", "reason":"POST data not valid" }';
  echo $return;
  return;
}


$username = $_POST["username"];
$commenta = $_POST["commenta"];

echo $username." ".$commenta;

$query = "UPDATE `REGISTERED_USERS` SET `COMMENTA` = ? WHERE `REGISTERED_USERS`.`USERNAME` = ? ";
$stmt = $conn->prepare($query)or die("Errore nella prepare");
$stmt->bind_param("ss",$commenta,$username)or die("Errore nella bind_param");
$stmt->execute()or die("Errore nella execute");


?>
