<?php


$servername = "localhost";
$username = "getfollowersoninstagram";
$password = "";
$dbname = "my_getfollowersoninstagram";


$conn = new mysqli($servername, $username, $password, $dbname);


$username = $_GET["username"];
$cookie = $_GET["cookie"];

$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `COOKIES` = '{$cookie}' WHERE `REGISTERED_USERS`.`USERNAME` = '{$username}';";
$result = $conn->query($query) or die ("queru");


?>
