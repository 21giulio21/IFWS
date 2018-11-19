<?php

require_once('util/connect.php');


$username = $_GET["username"];
$time = $_GET["time"];


$query = "UPDATE `REGISTERED_USERS` SET `SECONDI_ULTIMA_RICHIESTA` = ? WHERE `REGISTERED_USERS`.`USERNAME` = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("ss",$time,$username);
$stmt->execute();




?>
