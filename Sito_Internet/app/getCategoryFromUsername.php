<?php

require_once('../util/connect.php');
/*
Questo file permette di prendere in input la mail dell'utente e torna un json con tutti i dati dell'utente
in modo tale che possa sapere id dell'utente ecc...
*/

if(!isset($_POST["USERNAME"]))
{
  $return = '{ "success":"failed", "reason":"POST data not valid" }';
  echo $return;
  return;
}

$username = $_POST["USERNAME"];

// prima guardo se per caso c'è un altro utente con quella mail, nel caso dico che ho gia inserito
$query = "SELECT `TARGET` FROM `REGISTERED_USERS` WHERE `USERNAME` = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("s", $username);
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
