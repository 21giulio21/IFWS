
<?php
/*
Questo file prende in input la mail dell'utente e restituisce in output tutti gli account instagram a lui collegati

*/

require_once('../util/connect.php');

if(!isset($_POST["EMAIL"]))
{
  $return = '{ "success":"failed", "reason":"POST data not valid" }';
  echo $return;
  return;
}


$email = $_POST["EMAIL"];


// restituisco tutti gli gli account Instagram collegati a quella mail
$query = "SELECT * FROM `REGISTERED_USERS` WHERE `EMAIL` = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("s",$email);
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