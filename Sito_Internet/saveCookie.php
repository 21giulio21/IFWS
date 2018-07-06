<?php


require_once('util/connect.php');


$username = $_GET["username"];
$cookie = $_GET["cookie"];

$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `COOKIES` = '{$cookie}' WHERE `REGISTERED_USERS`.`USERNAME` = '{$username}';";
$result = $conn->query($query) or die ("Query non funzionante");


?>
