<?php


require_once('../util/connect.php');

/*
Questo file permette di eliminare l'account Instagram collegato alla mail presa come input e username
*/


$username = $_POST["USERNAME"];



$query = "DELETE FROM `REGISTERED_USERS` WHERE `REGISTERED_USERS`.`USERNAME` = ?";
$stmt = $conn->prepare($query);
$stmt->bind_param("s",$username);
$stmt->execute();


?>
