<?php


require_once('util/connect.php');


$username = $_GET["username"];
$cookie = $_GET["cookie"];

$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `COOKIES` = ? WHERE `REGISTERED_USERS`.`USERNAME` = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("ss",$cookie,$username);
$stmt->execute();


?>
