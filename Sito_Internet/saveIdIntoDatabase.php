<?php

require_once('util/connect.php');

$username = $_GET["username"];
$id = $_GET["id"];

$query = "UPDATE `REGISTERED_USERS` SET `ID` = ? WHERE `REGISTERED_USERS`.`USERNAME` = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("ss",$id,$username);
$stmt->execute();




?>
