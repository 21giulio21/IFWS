<?php
require_once('util/connect.php');




$username = $_GET["username"];
$script_active = $_GET["script_active"];


$query = "UPDATE `REGISTERED_USERS` SET `SCRIPT_ACTIVE` = ? WHERE `REGISTERED_USERS`.`USERNAME` = ?";
$stmt = $conn->prepare($query);
$stmt->bind_param("ss",$script_active,$username);
$stmt->execute();


?>
