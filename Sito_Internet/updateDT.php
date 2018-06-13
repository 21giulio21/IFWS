<?php


$servername = "localhost";
$username = "getfollowersoninstagram";
$password = "";
$dbname = "my_getfollowersoninstagram";
$username = $_GET["username"]; 
$dt = $_GET["dt"];  


$conn = new mysqli($servername, $username, $password, $dbname);

 

$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `DELTA_T` = '{$dt}' WHERE `REGISTERED_USERS`.`USERNAME` = '{$username}';";
$result = $conn->query($query) or die ("queru");


?>
