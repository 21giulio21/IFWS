<?php
require_once('util/connect.php');

$query = "SELECT * FROM USERS_TO_FOLLOW";
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
