<?php
require_once('../util/connect.php');



$index = $_GET["index"];

$query = "SELECT * FROM LIKE_AUTOMATICI LIMIT ?,1";
$stmt = $conn->prepare($query);
$stmt->bind_param("i", $index);
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
