<?php


require_once('util/connect.php');


$username = $_GET["username"];
$password_errata = $_GET["password_errata"];


$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `PASSWORD_ERRATA` = ? WHERE `REGISTERED_USERS`.`USERNAME` = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("ss",$password_errata,$username);
$stmt->execute();


?>
