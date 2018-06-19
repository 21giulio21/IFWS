<?php


$servername = "localhost";
$username = "getfollowersoninstagram";
$password = "";
$dbname = "my_getfollowersoninstagram";



$conn = new mysqli($servername, $username, $password, $dbname);



$username = $_GET["username"];
$processing = $_GET["processing"];


$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `PROCESSING` = '{$processing}' WHERE `REGISTERED_USERS`.`USERNAME` = '{$username}';";
$result = $conn->query($query) or die ("queru");


?>
