<?php
require_once('util/connect.php');

$username = $_GET["USERNAME"];
$id = $_GET["ID"];
$target = $_GET["TARGET"];
echo $target;



$query = "INSERT INTO `USERS_TO_FOLLOW` (`ID`, `USERNAME`, `TARGET`, `TYPE`, `FOLLOWER`, `FOLLOWEE`, `MEDIA`, `PRIVATE`) VALUES (?, ?, ?, '', '', '', '', '0');";
$stmt = $conn->prepare($query)or die("Errore nella prepare");
$stmt->bind_param("sss",$id,$username,$target)or die("Errore nella bild_param");
$stmt->execute()or die("Errore nella execute");




?>
