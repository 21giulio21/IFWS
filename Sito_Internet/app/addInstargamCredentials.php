<?php

require_once('../util/connect.php');




$username_instagram = $_POST["username"];
$password_instagram = $_POST["password_instagram"];
$email = $_POST["email"];



// Inserisco le credenziali dell'utente e imposto `PROCESSING` = '1' in questo modo lo
//script controllera che ho `PROCESSING` = '1' e lo processa per vedere se le credenziali
// di instagram inserite sono corrette
$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `USERNAME` = '{$username_instagram}',`DELTA_T` = '150', `PASSWORD_INSTAGRAM` = '{$password_instagram}', `PROCESSING` = '1' WHERE `REGISTERED_USERS`.`EMAIL` = '{$email}';";
$result = $conn->query($query) or die ("Query non funzionante");





?>
