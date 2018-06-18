<?php


$servername = "localhost";
$username = "getfollowersoninstagram";
$password = "";
$dbname = "my_getfollowersoninstagram";



$conn = new mysqli($servername, $username, $password, $dbname);


$username = $_GET["username"];
$dt = $_GET["dt"]; 


$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `DELTA_T` = '{$dt}' WHERE `REGISTERED_USERS`.`USERNAME` = '{$username}';";
$result = $conn->query($query) or die ("queru");


?>
