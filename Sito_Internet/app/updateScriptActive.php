<?php


require_once('../util/connect.php');



echo "ds";
$username = $_POST["username"];
$script_active = $_POST["script_active"];

print_r($_POST);


$query = "UPDATE `REGISTERED_USERS` SET `SCRIPT_ACTIVE` = ? WHERE `REGISTERED_USERS`.`USERNAME` = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("ss",$script_active,$username);
$stmt->execute();


?>
