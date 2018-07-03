<?php


$servername = "localhost";
$username = "getfollowersoninstagram";
$password = "";
$dbname = "my_getfollowersoninstagram";

$conn = new mysqli($servername, $username, $password, $dbname);


$index = $_GET["index"];



$query = "SELECT * FROM REGISTERED_USERS LIMIT {$index},1";
$result = $conn->query($query) or die ("queru");


$myArray = array();
while ($row = $result->fetch_object())
{
  $tempArray = $row;
  array_push($myArray, $tempArray);
}

echo json_encode($myArray);

?>
