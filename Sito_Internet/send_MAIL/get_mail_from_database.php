<?php
require_once('../util/connect.php');

/*
Questo file permette di ottenere una sola tupa dal database: SMS_INSTATRACK
*/

//Ottengo la prima tupla a cui mandare il messaggio
$query = "SELECT * FROM `MAIL_INSTATRACK` LIMIT 0,1";
$stmt = $conn->prepare($query);
$stmt->execute();
$result = get_result($stmt);
$myArray = array();
foreach ($result as $row)
{
  $tempArray = $row;
  array_push($myArray, $tempArray);
}
echo json_encode($myArray);
$id = $myArray[0]["ID"];
// Da qui devo rimuogere il messaggio.

$query = "DELETE FROM `MAIL_INSTATRACK` WHERE `MAIL_INSTATRACK`.`ID` = ? ";
$stmt = $conn->prepare($query)or die("Errore nella prepare");
$stmt->bind_param("s",$id)or die("Errore nella bind_param");
$stmt->execute()or die("Errore nella execute");


?>