<?php
require_once('util/connect.php');


$username = $_GET["username"];
$follow_unfollow = $_GET["follow_unfollow"];

$query = "UPDATE `REGISTERED_USERS` SET `FOLLOW_UNFOLLOW` = ? WHERE `REGISTERED_USERS`.`USERNAME` = ? ;";

$stmt = $conn->prepare($query);
$stmt->bind_param("ss",$follow_unfollow,$username);
$stmt->execute();



?>
