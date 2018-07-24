<?php


require_once('../util/connect.php');

/*
Questo file permette di ottenere tutte le categoria che devo permette all'utente di scegliere
*/

$query = "SELECT * FROM `CATEGORY`";
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


?>
