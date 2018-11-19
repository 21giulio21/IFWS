<?php


require_once('../util/connect.php');


if( !isset($_POST["USERNAME"]) || !isset($_POST["CATEGORY"]) )
{
  $return = '{ "success":"failed", "reason":"POST data not valid" }';
  echo $return;
  return;
}




$username = $_POST["USERNAME"];
$category = $_POST["CATEGORY"];


echo $username . $category;

$query = "UPDATE `REGISTERED_USERS` SET `TARGET` = ? WHERE `REGISTERED_USERS`.`USERNAME` = ? ";
$stmt = $conn->prepare($query)or die("Errore nella prepare");
$stmt->bind_param("ss",$category,$username)or die("Errore nella bind_param");
$stmt->execute()or die("Errore nella execute");


?>
