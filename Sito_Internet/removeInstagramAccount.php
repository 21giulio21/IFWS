<?php


$servername = "localhost";
$username = "getfollowersoninstagram";
$password = "";
$dbname = "my_getfollowersoninstagram";


$conn = new mysqli($servername, $username, $password, $dbname);

$username = $_POST["username"];
$newUsername = $_POST["newUsername"];

$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `USERNAME` = '{$newUsername}',  `ID` = '' ,`SECONDI_ULTIMA_RICHIESTA` = '0' ,`NUMBER_REQUESTS_DONE` = '0' , `COOKIES` = '', `USERS_FOLLOWED` = '', `PASSWORD_INSTAGRAM` = '', `URL_IMMAGINE_PROFILO` = '', `SCRIPT_ACTIVE` = '0' WHERE `REGISTERED_USERS`.`USERNAME` = '{$username}';";
$result = $conn->query($query) or die ("queru");


?>
