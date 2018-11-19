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
  $result = get_result($stmt);


  if (count($result) == 0 )
  {
      $stmt->close();
      $query = 'SELECT * FROM `USERS_TO_FOLLOW` WHERE `TARGET` = "CHIARAFERRAGNI" ORDER BY RAND() LIMIT 1';
      $stmt = $conn->prepare($query);
      $stmt->execute();
      $result = get_result($stmt);
      $stmt->store_result();

  }
}else{
  $query = "SELECT * FROM `USERS_TO_FOLLOW` ORDER BY RAND() LIMIT 1";
  $stmt = $conn->prepare($query);
  $stmt->execute();
  $result = get_result($stmt);
  $stmt->store_result();

}


$myArray = array();


foreach ($result as $row)
{
    $tempArray = $row;
	array_push($myArray, $tempArray);
}

echo json_encode($myArray);

?>