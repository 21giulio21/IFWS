<?php

require_once('util/connect.php');

$thread = $_GET["THREAD"];


$query = "SELECT COUNT(*) AS COUNT FROM REGISTERED_USERS WHERE `THREAD` = {$thread} ";
$result = $conn->query($query) or die ("Query non funzionante");
$data = $result->fetch_array(MYSQLI_NUM);
print_r($data[0]);

?>
