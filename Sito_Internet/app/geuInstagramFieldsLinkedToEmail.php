
<?php
/*
Questo file prende in input la mail dell'utente e restituisce in output tutti gli account instagram a lui collegati

*/

require_once('../util/connect.php');


$email = $_POST["EMAIL"];

// COntrollo che non sia vuoto il valore di $_POST["EMAIL"]
if(!isset($_POST["EMAIL"]))
{
  return;
}

// restituisco tutti gli gli account Instagram collegati a quella mail
$query = "SELECT * FROM `REGISTERED_USERS` WHERE `EMAIL` = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("s",$email);
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
