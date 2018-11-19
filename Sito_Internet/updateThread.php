<?php
require_once('util/connect.php');


$username = $_GET["username"];
$thread = $_GET["thread"];

$query = "UPDATE  `Sql1217972_5`.`REGISTERED_USERS` SET  `THREAD` = ? WHERE  `REGISTERED_USERS`.`USERNAME` =  ? ";

$stmt = $conn->prepare($query);
$stmt->bind_param("ss",$thread,$username);
$stmt->execute();



?>
