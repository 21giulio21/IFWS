<?php


$servername = "localhost";
$username = "getfollowersoninstagram";
$password = "";
$dbname = "my_getfollowersoninstagram";


$conn = new mysqli($servername, $username, $password, $dbname);

$username = $_GET["username"];
$follow_unfollow = $_GET["follow_unfollow"];

$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `FOLLOW_UNFOLLOW` = '{$follow_unfollow}' WHERE `REGISTERED_USERS`.`USERNAME` = '{$username}';";
$result = $conn->query($query) or die ("queru");


?>
