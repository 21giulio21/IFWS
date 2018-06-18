<?php

$servername = "localhost";
$username = "getfollowersoninstagram";
$password = "";
$dbname = "my_getfollowersoninstagram";
$conn = new mysqli($servername, $username, $password, $dbname);


$username = $_GET["username"];
$time = $_GET["time"];


$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `SECONDI_ULTIMA_RICHIESTA` = '{$time}' WHERE `REGISTERED_USERS`.`USERNAME` = '{$username}';";
$result = $conn->query($query) or die ("queru");



?>
