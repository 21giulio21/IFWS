<?php

require_once('util/connect.php');




$username = $_GET["username"];
$processing = $_GET["processing"];


$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `PROCESSING` = ? WHERE `REGISTERED_USERS`.`USERNAME` = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("ss",$processing,$username);
$stmt->execute();


?>
