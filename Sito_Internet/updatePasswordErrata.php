<?php


require_once('util/connect.php');


$username = $_GET["username"];
$password_errata = $_GET["password_errata"];


$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `PASSWORD_ERRATA` = '{$password_errata}' WHERE `REGISTERED_USERS`.`USERNAME` = '{$username}';";
$result = $conn->query($query) or die ("Query non funzionante");


?>
