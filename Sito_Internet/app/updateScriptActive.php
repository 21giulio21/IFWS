<?php


$servername = "localhost";
$username = "getfollowersoninstagram";
$password = "";
$dbname = "my_getfollowersoninstagram";



$conn = new mysqli($servername, $username, $password, $dbname);



$username = $_POST["username"];
$script_active = $_POST["script_active"];


$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `SCRIPT_ACTIVE` = '{$script_active}' WHERE `REGISTERED_USERS`.`USERNAME` = '{$username}';";
$result = $conn->query($query) or die ("queru");


?>
