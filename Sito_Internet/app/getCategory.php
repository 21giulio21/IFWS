<?php


require_once('../util/connect.php');

/*
Questo file permette di ottenere tutte le categoria che devo permette all'utente di scegliere
*/

$query = "SELECT * FROM `CATEGORY`";
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


?>