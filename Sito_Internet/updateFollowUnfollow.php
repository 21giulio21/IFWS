<?php


$servername = "localhost";
$username = "getfollowersoninstagram";
$password = "";
$dbname = "my_getfollowersoninstagram";
$username = $_GET["username"];
$follow_unfollow = $_GET["follow_unfollow"];

$conn = new mysqli($servername, $username, $password, $dbname);

 

$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `FOLLOW_UNFOLLOW` = '{$follow_unfollow}' WHERE `REGISTERED_USERS`.`USERNAME` = '{$username}';";
$result = $conn->query($query) or die ("queru");


?>
