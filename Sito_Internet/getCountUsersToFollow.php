<?php


$servername = "localhost";
$username = "getfollowersoninstagram";
$password = "";
$dbname = "my_getfollowersoninstagram";

$conn = new mysqli($servername, $username, $password, $dbname);

 

$query = "SELECT COUNT(*) AS COUNT FROM idnumeri";
$result = $conn->query($query) or die ("queru");
$data = $result->fetch_array(MYSQLI_NUM);   
print_r($data[0]);

?>
