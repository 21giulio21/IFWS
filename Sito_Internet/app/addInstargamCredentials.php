<?php


$servername = "localhost";
$username = "getfollowersoninstagram";
$password = "";
$dbname = "my_getfollowersoninstagram";

$username_instagram = $_POST["username"];
$password_instagram = $_POST["password_instagram"];
$email = $_POST["email"];


$conn = new mysqli($servername, $username, $password, $dbname);

// prima guardo se per caso c'è un altro utente con quella mail, nel caso dico che ho gia inserito
$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `USERNAME` = '{$username_instagram}', `PASSWORD_INSTAGRAM` = '{$password_instagram}' WHERE `REGISTERED_USERS`.`EMAIL` = '{$email}';";
$result = $conn->query($query) or die ("queru");





?>
