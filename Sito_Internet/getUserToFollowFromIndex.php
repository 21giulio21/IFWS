<?php


$servername = "localhost";
$username = "getfollowersoninstagram";
$password = "";
$dbname = "my_getfollowersoninstagram";
$index = $_GET["index"];
$conn = new mysqli($servername, $username, $password, $dbname);

 

$query = "SELECT * FROM idnumeri LIMIT {$index},1";
$result = $conn->query($query) or die ("queru");


$myArray = array();
while ($row = $result->fetch_object()) 
{
                $tempArray = $row;
                array_push($myArray, $tempArray);
            }
        echo json_encode($myArray);

?>
