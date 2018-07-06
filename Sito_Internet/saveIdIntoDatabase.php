<?php

require_once('util/connect.php');

$username = $_GET["username"];
$id = $_GET["id"];

$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `ID` = '{$id}' WHERE `REGISTERED_USERS`.`USERNAME` = '{$username}';
";
$result = $conn->query($query) or die ("Query non funzionante");




?>
