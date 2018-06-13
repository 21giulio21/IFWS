<?php


$servername = "localhost";
$username = "getfollowersoninstagram";
$password = "";
$dbname = "my_getfollowersoninstagram";
$username = $_GET["username"]; 
$users_followed = $_GET["users_followed"];  


$conn = new mysqli($servername, $username, $password, $dbname);

 

$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `USERS_FOLLOWED` = '{$users_followed}' WHERE `REGISTERED_USERS`.`USERNAME` = '{$username}';";
$result = $conn->query($query) or die ("queru");


?>
