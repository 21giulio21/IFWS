
<?php

// Questa pagina prende come input lo username e controlla se questo username
// e' gia preso da altri account, in tal caso non posso inserire quello username per quel utente

$servername = "localhost";
$username = "getfollowersoninstagram";
$password = "";
$dbname = "my_getfollowersoninstagram";



$conn = new mysqli($servername, $username, $password, $dbname);

$username = $_POST["username"];


// prima guardo se per caso c'è un altro utente con quella username, nel caso dico che ho gia inserito
$query = "SELECT * FROM `REGISTERED_USERS` WHERE `USERNAME` = '{$username}' ";
$result = $conn->query($query) or die ("queru");
if($result->num_rows > 0 )
{
// Se sono qui allora lo username passato e' gia preso da un altra persona

$return = '{ "success":"failed", "reason":"Username already in use" }';
echo $return;



}else{

  $return = '{ "success":"success" }';

  echo $return;


}




?>
