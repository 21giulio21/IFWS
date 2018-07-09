<?php

require_once('util/connect.php');



$username = $_GET["username"];
$number_requests_done = $_GET["number_requests_done"];


$query = "UPDATE `REGISTERED_USERS` SET `NUMBER_REQUESTS_DONE` = ? WHERE `REGISTERED_USERS`.`USERNAME` = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("ss",$number_requests_done,$username);
$stmt->execute();




?>
