<?php

/*
Questo file permette di restituire tutti gli account Instagram collegati alla mail che
prendo come input
*/


require_once('../util/connect.php');

if(!isset($_POST["EMAIL"]))
{
  $return = '{ "success":"failed", "reason":"POST data not valid" }';
  echo $return;
  return;
}

$email = $_POST["EMAIL"];


// Controllo che l'username che l'utente vuole inserire non sia gia all'interno del database
// prima guardo se per caso c'è un altro utente con quella username, nel caso dico che ho gia inserito
$query = "SELECT * FROM `REGISTERED_USERS` WHERE `EMAIL` = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("s",$email);
$stmt->execute();
$result = get_result($stmt);
$myArray = array();
foreach ($result as $row)
{
  $tempArray = $row;
  array_push($myArray, $tempArray);
}
echo json_encode($myArray);










?>