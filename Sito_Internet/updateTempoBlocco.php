<?php


require_once('util/connect.php');



$username = $_GET["username"];
$tempo_blocco = $_GET["tempo_blocco"];


$query = "UPDATE `my_getfollowersoninstagram`.`REGISTERED_USERS` SET `TEMPO_ATTESA_BLOCCO` = '{$tempo_blocco}' WHERE `REGISTERED_USERS`.`USERNAME` = '{$username}';";
$result = $conn->query($query) or die ("Query non funzionante");


?>
