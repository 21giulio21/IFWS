<?php
require_once('util/connect.php');

// username della persona che desidera seguirne un'altra
$username_whants_to_follow = $_GET["USERNAME"];

$query = "SELECT USERS_TO_FOLLOW.USERNAME,USERS_TO_FOLLOW.ID,USERS_TO_FOLLOW.TARGET
    			FROM `USERS_TO_FOLLOW` INNER JOIN `REGISTERED_USERS`
          ON REGISTERED_USERS.TARGET=USERS_TO_FOLLOW.TARGET
          WHERE REGISTERED_USERS.USERNAME = '{$username_whants_to_follow}'
          ORDER BY RAND() LIMIT 1";


$result = $conn->query($query) or die ("Query non funzionante");

if (mysql_num_rows($result)==0) {

  $query = "	SELECT `USERNAME`, `ID` FROM `USERS_TO_FOLLOW` ORDER BY RAND() LIMIT 1";
	$result = $conn->query($query) or die ("Query non funzionante");
}

$myArray = array();


while ($row = $result->fetch_object())
{
    $tempArray = $row;
	array_push($myArray, $tempArray);
}

echo json_encode($myArray);

?>
