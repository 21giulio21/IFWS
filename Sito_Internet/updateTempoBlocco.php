<?php


$servername = "localhost";
$username = "getfollowersoninstagram";
$password = "";
$dbname = "my_getfollowersoninstagram";
$username = $_GET["username"]; 
$tempo_blocco = $_GET["tempo_blocco"];  


$conn = new mysqli($servername, $username, $password, $dbname);

 

$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `TEMPO_ATTESA_BLOCCO` = '{$tempo_blocco}' WHERE `REGISTERED_USERS`.`USERNAME` = '{$username}';";
$result = $conn->query($query) or die ("queru");


?>
