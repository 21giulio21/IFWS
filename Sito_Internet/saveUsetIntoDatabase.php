<?php
$id = $_GET["id"];
$username_profilo = $_GET["username"];


$servername = "localhost";
$username = "getfollowersoninstagram";
$password = "";
$dbname = "my_getfollowersoninstagram";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "INSERT INTO USERS_TO_FOLLOW VALUES ('{$id}', '{$username_profilo}');";
$result = $conn->query($sql);


?>
