<?php


require_once('../util/connect.php');




$username = $_POST["username"];
$commenta = $_POST["commenta"];

$query = "UPDATE `REGISTERED_USERS` SET `COMMENTA` = ? WHERE `REGISTERED_USERS`.`USERNAME` = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("ss",$commenta,$username);
$stmt->execute();


?>
