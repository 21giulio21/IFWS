<?php
require_once('../util/connect.php');

/*
Questo file permette di ottenere una sola tupa dal database: SMS_INSTATRACK
*/

//Ottengo la prima tupla a cui mandare il messaggio
$query = "SELECT * FROM `SMS_INSTATRACK` LIMIT 0,1";
$stmt = $conn->prepare($query);
$stmt->execute();
$result = $stmt->get_result();
$myArray = array();
while ($row = $result->fetch_object())
{
  $tempArray = $row;
  array_push($myArray, $tempArray);
}
echo json_encode($myArray);

// TODO: Da qui devo rimuogere il messaggio.


?>
