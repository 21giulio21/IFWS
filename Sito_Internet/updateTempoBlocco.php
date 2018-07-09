<?php


require_once('util/connect.php');



$username = $_GET["username"];
$tempo_blocco = $_GET["tempo_blocco"];


$query = "UPDATE `REGISTERED_USERS` SET `TEMPO_ATTESA_BLOCCO` = ? WHERE `REGISTERED_USERS`.`USERNAME` = ?";
$stmt = $conn->prepare($query);
$stmt->bind_param("ss",$tempo_blocco,$username);
$stmt->execute();

?>
