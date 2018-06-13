<?php


$servername = "localhost";
$username = "getfollowersoninstagram";
$password = "";
$dbname = "my_getfollowersoninstagram";
$username = $_GET["username"];
$cookie = $_GET["cookie"];

$conn = new mysqli($servername, $username, $password, $dbname);

$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `COOKIES` = '{$cookie}' WHERE `REGISTERED_USERS`.`USERNAME` = '{$username}';";
$result = $conn->query($query) or die ("queru");


?>
