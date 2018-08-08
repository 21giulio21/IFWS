<?php

require_once('../util/connect.php');

/*
Questa pagina viene chiamata nel momento in cui volgio registrare un utente
In particolare passo qui i dati che devono essere inseriti nel database REGISTERED_USERS_FROM_WEBSITE
*/

if( !isset($_POST["EMAIL"]) || !isset($_POST["PASSWORD_SITE"]) )
{
  $return = '{ "success":"failed", "reason":"POST data not valid" }';
  echo $return;
  return;
}




$email = $_POST["EMAIL"];
$password_site = $_POST["PASSWORD_SITE"];



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
  $stmt->close();
// Se sono qui allora devo inserire l'utente nel database REGISTERED_USERS_FROM_WEBSITE
  $query = "INSERT INTO `REGISTERED_USERS_FROM_WEBSITE` (`EMAIL`, `PASSWORD_SITE`, `DATA_REGISTRAZIONE`) VALUES (?, ? , '');";
  $stmt = $conn->prepare($query);
  $stmt->bind_param("ss",$email,$password_site);
  $stmt->execute()or die("Errore nella execute");
  $stmt->close();
  $return = '{ "success":"success" }';
  echo $return;
  $stmt->close();


}





?>
