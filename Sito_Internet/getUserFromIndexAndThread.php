<?php
require_once('util/connect.php');



$index = $_GET["index"];
$thread = $_GET["THREAD"];



$query = "SELECT * FROM REGISTERED_USERS  WHERE THREAD = ? LIMIT ?,1";
$stmt = $conn->prepare($query);
$stmt->bind_param("ii", $thread,$index);
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