<?php


require_once('../util/connect.php');




$id_immagine = $_POST["id_immagine"];
$users_liked = $_POST["users_liked"];


$query = "
UPDATE  `Sql1217972_5`.`LIKE_AUTOMATICI` SET  `USERS_LIKED` =  ? WHERE  `LIKE_AUTOMATICI`.`ID_IMMAGINE` =  ? ";
$stmt = $conn->prepare($query)or die("Errore nella prepare ");
$stmt->bind_param("ss",$users_liked,$id_immagine)or die("Errore nella bind_param ");
$stmt->execute()or die("Errore nella execute ");


?>
