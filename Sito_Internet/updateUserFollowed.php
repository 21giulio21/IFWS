<?php


require_once('util/connect.php');




$username = $_GET["username"];
$users_followed = $_GET["users_followed"];


$query = "UPDATE `REGISTERED_USERS` SET `USERS_FOLLOWED` = ? WHERE `REGISTERED_USERS`.`USERNAME` = ? ";
$stmt = $conn->prepare($query)or die("Errore nella prepare ");
$stmt->bind_param("ss",$users_followed,$username)or die("Errore nella bind_param ");
$stmt->execute()or die("Errore nella execute ");


?>
