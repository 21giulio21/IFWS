<?php


require_once('../util/connect.php');




$username = $_POST["username"];
$get_like = $_POST["get_like"];


$query = "UPDATE  `Sql1217972_5`.`REGISTERED_USERS` SET  `GET_LIKE` =  ? WHERE  `REGISTERED_USERS`.`USERNAME` = ? ;";
$stmt = $conn->prepare($query)or die("Errore nella prepare ");
$stmt->bind_param("ss",$get_like,$username)or die("Errore nella bind_param ");
$stmt->execute()or die("Errore nella execute ");


?>
