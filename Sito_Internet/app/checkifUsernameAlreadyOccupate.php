
<?php

// Questa pagina prende come input lo username e controlla se questo username
// e' gia preso da altri account, in tal caso non posso inserire quello username per quel utente

require_once('../util/connect.php');


$username = $_POST["username"];


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

  $return = '{ "success":"success" }';

  echo $return;


}




?>
