<?php

$servername = "localhost";
$username = "getfollowersoninstagram";
$password = "";
$dbname = "my_getfollowersoninstagram";




$conn = new mysqli($servername, $username, $password, $dbname);


$username = $_GET["username"];
$number_requests_done = $_GET["number_requests_done"]; 


$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `NUMBER_REQUESTS_DONE` = '{$number_requests_done}' WHERE `REGISTERED_USERS`.`USERNAME` = '{$username}';";
$result = $conn->query($query) or die ("queru");



?>
