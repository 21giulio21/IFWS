<?php
require_once('util/connect.php');

$username = $_GET["USERNAME"];
$id = $_GET["ID"];
$target = $_GET["TARGET"];
$follower = $_GET["FOLLOWER"];
$followee = $_GET["FOLLOWEE"];
$media = $_GET["MEDIA"];
$type = $_GET["TYPE"];
$private = $_GET["PRIVATE"];


$query = "INSERT INTO `my_getfollowersoninstagram`.`USERS_TO_FOLLOW` (`ID`, `USERNAME`, `TARGET`, `TYPE`, `FOLLOWER`, `FOLLOWEE`, `MEDIA`, `PRIVATE`) VALUES ('{$id}', '{$username}', '{$target}', '{$type}', '{$follower}', '{$followee}', '{$media}','{$private}');";
$result = $conn->query($query) or die ("Query non funzionante");




?>
