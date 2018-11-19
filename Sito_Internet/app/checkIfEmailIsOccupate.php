<?php
require_once('../util/connect.php');

/*
Questa pagina viene chiamata nel momento in cui volgio registrare un utente
Prima di verificarlo controllo che la mail non sia gia occupata.
*/

if( !isset($_POST["EMAIL"]) )
{
  $return = '{ "success":"failed", "reason":"POST data not valid" }';
  echo $return;
  return;
}


$email = $_POST["EMAIL"];



// prima guardo se per caso c'è un altro utente con quella mail, nel caso dico che ho gia inserito
$query = "SELECT * FROM `REGISTERED_USERS_FROM_WEBSITE` WHERE `EMAIL` = ? ";
$stmt = $conn->prepare($query) or die("Errore nella prepare");
$stmt->bind_param("s",$email) or die("Errore nella bind_param");
$stmt->execute() or die("Errore nella execute");
$stmt->store_result();
if($stmt->num_rows == 1  )
{
// Se sono qui allora ho gia inserito un utente con quell'username
$return = '{ "success":"failed", "reason":"Email already in use" }';
echo $return;

}else{
  $return = '{ "success":"success" }';
  echo $return;


}
