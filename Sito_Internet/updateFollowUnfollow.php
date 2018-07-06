<?php
require_once('util/connect.php');


$username = $_GET["username"];
$follow_unfollow = $_GET["follow_unfollow"];

$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `FOLLOW_UNFOLLOW` = '{$follow_unfollow}' WHERE `REGISTERED_USERS`.`USERNAME` = '{$username}';";
$result = $conn->query($query) or die ("Query non funzionante");


?>
