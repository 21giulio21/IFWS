<?php
require_once('util/connect.php');



$index = $_GET["index"];

$query = "SELECT * FROM REGISTERED_USERS LIMIT ?,1";
$stmt = $conn->prepare($query);
$stmt->bind_param("i", $index);
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
