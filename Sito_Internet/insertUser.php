<?php


$servername = "localhost";
$username = "getfollowersoninstagram";
$password = "";
$dbname = "my_getfollowersoninstagram";

$conn = new mysqli($servername, $username, $password, $dbname);

 

$query = "SELECT * FROM idnumeri";
$result = $conn->query($query) or die ("queru");


$myArray = array();
while ($row = $result->fetch_object()) 
{
                $tempArray = $row;
                array_push($myArray, $tempArray);
            }
        echo json_encode($myArray);

?>