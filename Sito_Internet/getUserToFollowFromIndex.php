<?php
require_once('util/connect.php');
$index = $_GET["index"];



$query = "SELECT * FROM USERS_TO_FOLLOW LIMIT {$index},1";
$result = $conn->query($query) or die ("Query non funzionante");


$myArray = array();
while ($row = $result->fetch_object())
{
                $tempArray = $row;
                array_push($myArray, $tempArray);
            }
        echo json_encode($myArray);

?>
