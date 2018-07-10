<?php

require_once('../util/connect.php');




$username_instagram = $_POST["USERNAME"];
$password_instagram = $_POST["PASSWORD_INSTAGRAM"];
$email = $_POST["EMAIL"];


// Controllo che l'username che l'utente vuole inserire non sia gia all'interno del database
// prima guardo se per caso c'è un altro utente con quella username, nel caso dico che ho gia inserito
$query = "SELECT * FROM `REGISTERED_USERS` WHERE `USERNAME` = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("s",$username);
$stmt->execute();
$stmt->store_result();

if ($stmt->num_rows == 1 )
{
// Se sono qui allora lo username passato e' gia preso da un altra persona

$return = '{ "success":"failed", "reason":"Username already in use" }';
echo $return;



}else{

  // Inserisco le credenziali dell'utente e imposto `PROCESSING` = '1' in questo modo lo
  //script controllera che ho `PROCESSING` = '1' e lo processa per vedere se le credenziali
  // di instagram inserite sono corrette
  $query = "UPDATE `REGISTERED_USERS` SET `USERNAME` = ?  ,`DELTA_T` = '200', `PASSWORD_INSTAGRAM` = ? , `PROCESSING` = '1' WHERE `REGISTERED_USERS`.`EMAIL` = ? ";
  $stmt = $conn->prepare($query);
  $stmt->bind_param("sss",$username_instagram,$password_instagram,$email);
  $stmt->execute();
  $stmt->store_result();

  $return = '{ "success":"success" }';

  echo $return;


}








?>
