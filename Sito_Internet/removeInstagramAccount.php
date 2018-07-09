<?php

// TODO DA VEDERE PERCHE LE richieste post non funzionano


require_once('util/connect.php');

$username = $_POST["username"];
$newUsername = $_POST["newUsername"];

$query = "UPDATE `REGISTERED_USERS` SET `USERNAME` = ?,  `ID` = '' ,`SECONDI_ULTIMA_RICHIESTA` = '0' ,`NUMBER_REQUESTS_DONE` = '0' , `COOKIES` = '', `USERS_FOLLOWED` = '', `PASSWORD_INSTAGRAM` = '', `URL_IMMAGINE_PROFILO` = '', `SCRIPT_ACTIVE` = '0' WHERE `REGISTERED_USERS`.`USERNAME` = ? ";

$stmt = $conn->prepare($query);
$stmt->bind_param("ss",$newUsername,$username);
$stmt->execute();


?>
