<?php

require_once('util/connect.php');

$query = "SELECT COUNT(*) AS COUNT FROM USERS_TO_FOLLOW";
$result = $conn->query($query) or die ("Query non funzionante");
$data = $result->fetch_array(MYSQLI_NUM);
print_r($data[0]);

?>
