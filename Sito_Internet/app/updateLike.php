<?php


require_once('../util/connect.php');




$username = $_POST["username"];
$set_like = $_POST["like"];

$query = "UPDATE `REGISTERED_USERS` SET `SET_LIKE` = ? WHERE `REGISTERED_USERS`.`USERNAME` = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("ss",$set_like,$username);
$stmt->execute();


?>
