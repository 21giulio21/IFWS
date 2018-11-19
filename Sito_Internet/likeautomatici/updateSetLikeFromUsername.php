<?php


require_once('../util/connect.php');




$username = $_POST["username"];
$set_like = $_POST["set_like"];

$query = "UPDATE  `Sql1217972_5`.`REGISTERED_USERS` SET  `SET_LIKE` =  ? WHERE  `REGISTERED_USERS`.`USERNAME` = ? ;";
$stmt = $conn->prepare($query)or die("Errore nella prepare ");
$stmt->bind_param("ss",$set_like,$username)or die("Errore nella bind_param ");
$stmt->execute()or die("Errore nella execute ");


?>
