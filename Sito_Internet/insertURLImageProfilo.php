<?php

require_once('util/connect.php');

$username = $_GET["username"];
$immagine_profilo= $_GET["immagine_profilo"];


$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `URL_IMMAGINE_PROFILO` = '{$immagine_profilo}' WHERE `REGISTERED_USERS`.`USERNAME` = '{$username}';";
$result = $conn->query($query) or die ("Query non funzionante");


?>
