<?php


require_once('util/connect.php');




$username = $_GET["username"];
$users_followed = $_GET["users_followed"];


$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `USERS_FOLLOWED` = ? WHERE `REGISTERED_USERS`.`USERNAME` = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("ss",$users_followed,$username);
$stmt->execute();


?>
