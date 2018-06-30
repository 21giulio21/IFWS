<?php


$servername = "localhost";
$username = "getfollowersoninstagram";
$password = "";
$dbname = "my_getfollowersoninstagram";
$conn = new mysqli($servername, $username, $password, $dbname);

$target = $_GET["TARGET"];
// username della persona che desidera seguirne un'altra
$username_whants_to_follow = $_GET["USERNAME"];


// nel caso in cui il target è nullo allora prendo un utente casuale di qualsiasi target
if($target == "")
{
//in questo caso il target non è settato, devo seguire un utente che ha un qualsiasi target
	$query = "	SELECT USERS_TO_FOLLOW.USERNAME,USERS_TO_FOLLOW.ID 
    			FROM `USERS_TO_FOLLOW` INNER JOIN `REGISTERED_USERS_NUOVA` 
                ON REGISTERED_USERS_NUOVA.TARGET=USERS_TO_FOLLOW.TARGET 
                WHERE REGISTERED_USERS_NUOVA.USERNAME = '{$username_whants_to_follow}' ORDER BY RAND() LIMIT 1";
	$result = $conn->query($query) or die ("Query non funzionante");


}else
{
// in uqesto caso il target è settato e devo seguire un utente di quel target

	$query = "	SELECT USERS_TO_FOLLOW.USERNAME,USERS_TO_FOLLOW.ID 
    			FROM `USERS_TO_FOLLOW` INNER JOIN `REGISTERED_USERS_NUOVA` 
                ON REGISTERED_USERS_NUOVA.TARGET=USERS_TO_FOLLOW.TARGET 
                WHERE REGISTERED_USERS_NUOVA.USERNAME = '{$username_whants_to_follow}' ORDER BY RAND() LIMIT 1";
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
