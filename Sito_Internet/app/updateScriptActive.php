<?php


require_once('../util/connect.php');


if( !isset($_POST["username"]) || !isset($_POST["script_active"]) )
{
  $return = '{ "success":"failed", "reason":"POST data not valid" }';
  echo $return;
  return;
}
$username = $_POST["username"];
$script_active = $_POST["script_active"];

echo $username." ".$script_active;



$query = "UPDATE `REGISTERED_USERS` SET `SCRIPT_ACTIVE` = ? WHERE `REGISTERED_USERS`.`USERNAME` = ? ";
$stmt = $conn->prepare($query)or die("Errore nella prepare");
$stmt->bind_param("ss",$script_active,$username)or die("Errore nella bind_param");
$stmt->execute()or die("Errore nella execute");


?>
