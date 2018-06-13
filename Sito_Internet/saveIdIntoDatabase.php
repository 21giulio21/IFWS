<?php


$servername = "localhost";
$username = "getfollowersoninstagram";
$password = "";
$dbname = "my_getfollowersoninstagram";
$username = $_GET["username"];
$id = $_GET["id"];


$conn = new mysqli($servername, $username, $password, $dbname);

 

$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `ID` = '{$id}' WHERE `REGISTERED_USERS`.`USERNAME` = '{$username}';
";
$result = $conn->query($query) or die ("queru");




?>
