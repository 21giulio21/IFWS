<?php


$servername = "localhost";
$username = "getfollowersoninstagram";
$password = "";
$dbname = "my_getfollowersoninstagram";



$conn = new mysqli($servername, $username, $password, $dbname);



$username = $_GET["username"];
$password_errata = $_GET["password_errata"];


$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `PASSWORD_ERRATA` = '{$password_errata}' WHERE `REGISTERED_USERS`.`USERNAME` = '{$username}';";
$result = $conn->query($query) or die ("queru");


?>
