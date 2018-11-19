<?php

require_once('util/connect.php');


$username = $_GET["username"];

$query = "SELECT * FROM `REGISTERED_USERS` WHERE `USERNAME` = ? ";
$stmt = $conn->prepare($query)or die("Errore nella prepare");
$stmt->bind_param("s", $username);
$stmt->execute()or die("Errore nella execute");
$result = get_result($stmt);
$myArray = array();
foreach ($result as $row)
{
  $tempArray = $row;
  array_push($myArray, $tempArray);
}
echo json_encode($myArray);

?>