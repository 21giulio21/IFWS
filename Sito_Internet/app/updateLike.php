<?php


require_once('../util/connect.php');

if( !isset($_POST["username"]) || !isset($_POST["like"]) )
{
  $return = '{ "success":"failed", "reason":"POST data not valid" }';
  echo $return;
  return;
}



$username = $_POST["username"];
$set_like = $_POST["like"];

echo $username." ".$set_like;

$query = "UPDATE `REGISTERED_USERS` SET `SET_LIKE` = ? WHERE `REGISTERED_USERS`.`USERNAME` = ? ";
$stmt = $conn->prepare($query)or die("Errore nella prepare");
$stmt->bind_param("ss",$set_like,$username)or die("Errore nella bind_param");
$stmt->execute()or die("Errore nella execute");


?>
