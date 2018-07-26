<?php
require_once('util/connect.php');

// target richiesto
$target = $_GET["target"];
if(!empty($target))
{
  $query = "SELECT * FROM `USERS_TO_FOLLOW` WHERE `TARGET` = ? ORDER BY RAND() LIMIT 1";
  $stmt = $conn->prepare($query);
  $stmt->bind_param("s", $target);
  $stmt->execute();
  $result = $stmt->get_result();
  $stmt->store_result();

}else{
  $query = "SELECT * FROM `USERS_TO_FOLLOW` ORDER BY RAND() LIMIT 1";
  $stmt = $conn->prepare($query);
  $stmt->execute();
  $result = $stmt->get_result();
  $stmt->store_result();

}


$myArray = array();


while ($row = $result->fetch_object())
{
    $tempArray = $row;
	array_push($myArray, $tempArray);
}

echo json_encode($myArray);

?>
