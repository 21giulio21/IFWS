<?php


require_once('util/connect.php');


$id = $_GET["id"];
$username_profilo = $_GET["username"];

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "INSERT INTO USERS_TO_FOLLOW VALUES (? , ? );";
$stmt = $conn->prepare($query);
$stmt->bind_param("ss",$id,$username_profilo);
$stmt->execute();


?>
