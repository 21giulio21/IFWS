<?php

require_once('../util/connect.php');
/*
Questo file permette di prendere in input la mail dell'utente e torna un json con tutti i dati dell'utente
in modo tale che possa sapere id dell'utente ecc...
*/
$email = $_POST["EMAIL"];

// prima guardo se per caso c'è un altro utente con quella mail, nel caso dico che ho gia inserito
$query = "SELECT * FROM `REGISTERED_USERS_FROM_WEBSITE` WHERE `EMAIL` = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("s", $email);
$stmt->execute();
$result = $stmt->get_result();
$myArray = array();
while ($row = $result->fetch_object())
{
  $tempArray = $row;
  array_push($myArray, $tempArray);
}
echo json_encode($myArray);


?>
