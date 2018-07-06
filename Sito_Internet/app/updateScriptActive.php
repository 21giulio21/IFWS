<?php


require_once('../util/connect.php');




$username = $_POST["username"];
$script_active = $_POST["script_active"];


$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `SCRIPT_ACTIVE` = '{$script_active}' WHERE `REGISTERED_USERS`.`USERNAME` = '{$username}';";
$result = $conn->query($query) or die ("Query non funzionante");


?>
