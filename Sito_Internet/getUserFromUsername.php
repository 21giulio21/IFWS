<?php
echo "sss";

require_once('util/connect.php');



$username = $_GET["username"];

echo "string";

$query = "SELECT * FROM `REGISTERED_USERS` WHERE `USERNAME` = ? ";
$stmt = $conn->prepare($query)or die("Errore nella prepare");
//$stmt->bind_param("s", $username);
$stmt->execute()or die("Errore nella execute");
$result = $stmt->get_result();
$myArray = array();
while ($row = $result->fetch_object())
{
  $tempArray = $row;
  array_push($myArray, $tempArray);
}
echo json_encode($myArray);

?>
