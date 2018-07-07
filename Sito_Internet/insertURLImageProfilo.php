<?php

require_once('util/connect.php');

$username = $_GET["username"];
$immagine_profilo= $_GET["immagine_profilo"];


$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `URL_IMMAGINE_PROFILO` = ? WHERE `REGISTERED_USERS`.`USERNAME` = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("ss",$immagine_profilo,$username);
$stmt->execute();


?>
