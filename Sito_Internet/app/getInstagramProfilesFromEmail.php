<?php

/*
Questo file permette di restituire tutti gli account Instagram collegati alla mail che
prendo come input
*/


require_once('../util/connect.php');


$email = $_POST["EMAIL"];


// Controllo che l'username che l'utente vuole inserire non sia gia all'interno del database
// prima guardo se per caso c'è un altro utente con quella username, nel caso dico che ho gia inserito
$query = "SELECT * FROM `REGISTERED_USERS` WHERE `EMAIL` = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("s",$email);
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
