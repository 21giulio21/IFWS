<?php
require_once('util/connect.php');




$username = $_GET["username"];
$deve_pagare = $_GET["DEVE_PAGARE"];


$query = "UPDATE `REGISTERED_USERS` SET `DEVE_PAGARE` = ? WHERE `REGISTERED_USERS`.`USERNAME` = ?";
$stmt = $conn->prepare($query);
$stmt->bind_param("ss",$deve_pagare,$username);
$stmt->execute();


?>
