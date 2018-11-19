<?php
require_once('../util/connect.php');


$username = $_POST["username"];
$id_immagine = $_POST["id_immagine"];

$query = "INSERT INTO `Sql1217972_5`.`LIKE_AUTOMATICI` (`ID_IMMAGINE`, `USERNAME_IMMAGINE`, `USERS_LIKED`) VALUES (?, ?, '');";

$stmt = $conn->prepare($query);
$stmt->bind_param("ss",$id_immagine,$username);
$stmt->execute();



?>
