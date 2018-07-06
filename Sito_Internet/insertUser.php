<?php
require_once('util/connect.php');



$query = "SELECT * FROM USERS_TO_FOLLOW";
$result = $conn->query($query) or die ("Query non funzionante");


$myArray = array();
while ($row = $result->fetch_object())
{
                $tempArray = $row;
                array_push($myArray, $tempArray);
            }
        echo json_encode($myArray);

?>
