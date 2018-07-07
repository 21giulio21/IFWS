<?php
require_once('util/connect.php');

// username della persona che desidera seguirne un'altra
$username_whants_to_follow = $_GET["USERNAME"];

$query = "SELECT USERS_TO_FOLLOW.USERNAME,USERS_TO_FOLLOW.ID,USERS_TO_FOLLOW.TARGET
    			FROM `USERS_TO_FOLLOW` INNER JOIN `REGISTERED_USERS`
          ON REGISTERED_USERS.TARGET=USERS_TO_FOLLOW.TARGET
          WHERE REGISTERED_USERS.USERNAME = ?
          ORDER BY RAND() LIMIT 1";

$stmt = $conn->prepare($query);
$stmt->bind_param("s", $username_whants_to_follow);
$stmt->execute();
$result = $stmt->get_result();
$stmt->store_result();

if ($stmt->num_rows == 0) {

  $query = "SELECT `USERNAME`, `ID` FROM `USERS_TO_FOLLOW` ORDER BY RAND() LIMIT 1";
  $stmt = $conn->prepare($query);
  $stmt->execute();
  $result = $stmt->get_result();

}

$myArray = array();


while ($row = $result->fetch_object())
{
    $tempArray = $row;
	array_push($myArray, $tempArray);
}

echo json_encode($myArray);

?>
