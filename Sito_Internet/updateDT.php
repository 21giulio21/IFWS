<?php

require_once('util/connect.php');



$username = $_GET["username"];
$dt = $_GET["dt"];


$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `DELTA_T` = '{$dt}' WHERE `REGISTERED_USERS`.`USERNAME` = '{$username}';";
$result = $conn->query($query) or die ("Query non funzionante");


?>
