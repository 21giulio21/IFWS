<?php

require_once('util/connect.php');




$username = $_GET["username"];
$processing = $_GET["processing"];


$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `PROCESSING` = '{$processing}' WHERE `REGISTERED_USERS`.`USERNAME` = '{$username}';";
$result = $conn->query($query) or die ("Query non funzionante");


?>
