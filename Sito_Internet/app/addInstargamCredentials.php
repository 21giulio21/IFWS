<?php

require_once('../util/connect.php');




$username_instagram = $_POST["username"];
$password_instagram = $_POST["password_instagram"];
$email = $_POST["email"];



// Inserisco le credenziali dell'utente e imposto `PROCESSING` = '1' in questo modo lo
//script controllera che ho `PROCESSING` = '1' e lo processa per vedere se le credenziali
// di instagram inserite sono corrette
$query = "UPDATE `REGISTERED_USERS` SET `USERNAME` = ?  ,`DELTA_T` = '200', `PASSWORD_INSTAGRAM` = ? , `PROCESSING` = '1' WHERE `REGISTERED_USERS`.`EMAIL` = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("sss",$username_instagram,$password_instagram,$email);
$stmt->execute();
$stmt->store_result();





?>
