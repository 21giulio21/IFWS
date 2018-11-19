<?php

require_once('util/connect.php');



$username = $_GET["username"];
$dt = $_GET["dt"];


$query = "UPDATE `REGISTERED_USERS` SET `DELTA_T` = ? WHERE `REGISTERED_USERS`.`USERNAME` = ? ;";

$stmt = $conn->prepare($query);
$stmt->bind_param("ss",$dt,$username);
$stmt->execute();


?>
