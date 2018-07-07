<?php


require_once('../util/connect.php');


$username= $_POST["username"];


// prima guardo se per caso c'è un altro utente con quella mail, nel caso dico che ho gia inserito
$query = "SELECT * FROM `REGISTERED_USERS` WHERE `USERNAME` = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("s", $username);
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
