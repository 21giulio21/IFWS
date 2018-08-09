<?php
require_once('util/connect.php');



$index = $_GET["index"];
$thread = $_GET["THREAD"];



$query = "SELECT * FROM REGISTERED_USERS  WHERE THREAD = ? LIMIT ?,1";
$stmt = $conn->prepare($query);
$stmt->bind_param("ii", $thread,$index);
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
