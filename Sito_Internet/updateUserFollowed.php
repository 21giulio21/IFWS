<?php


require_once('util/connect.php');




$username = $_GET["username"];
$users_followed = $_GET["users_followed"];


$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `USERS_FOLLOWED` = '{$users_followed}' WHERE `REGISTERED_USERS`.`USERNAME` = '{$username}';";
$result = $conn->query($query) or die ("Query non funzionante");


?>
