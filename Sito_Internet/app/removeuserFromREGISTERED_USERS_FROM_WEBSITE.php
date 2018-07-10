<?php


require_once('../util/connect.php');

/*
Questo file permette di eliminare l'account isnerito dal sito.
Elimino l'account dal database REGISTERED_USERS_FROM_WEBSITE
*/


$email = $_POST["EMAIL"];



$query = "DELETE FROM `REGISTERED_USERS_FROM_WEBSITE` WHERE `REGISTERED_USERS_FROM_WEBSITE`.`EMAIL` = ?";
$stmt = $conn->prepare($query);
$stmt->bind_param("s",$email);
$stmt->execute();


?>
