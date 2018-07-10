<?php

require_once('../util/connect.php');

/*
Questa pagina viene chiamata nel momento in cui volgio registrare un utente
In particolare passo qui i dati che devono essere inseriti nel database REGISTERED_USERS_FROM_WEBSITE

*/

$email = $_POST["EMAIL"];
$password_site = $_POST["PASSWORD_SITE"];



// prima guardo se per caso c'è un altro utente con quella mail, nel caso dico che ho gia inserito
$query = "SELECT * FROM REGISTERED_USERS WHERE EMAIL = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("s",$email);
$stmt->execute();
$stmt->close();
if($stmt->num_rows == 1  )
{
// Se sono qui allora ho gia inserito un utente con quell'username
$return = '{ "success":"failed", "reason":"Email already in use" }';
echo $return;

}else{

// Se sono qui allora devo inserire l'utente nel database REGISTERED_USERS_FROM_WEBSITE
  $query = "INSERT INTO `REGISTERED_USERS_FROM_WEBSITE` (`EMAIL`, `PASSWORD_SITE`, `ID_UTENTE`, `DATA_REGISTRAZIONE`) VALUES (?, ? , NULL, '');";
  $stmt = $conn->prepare($query);
  $stmt->bind_param("ss",$email,$password_site);
  $stmt->execute()or die("Errore nella execute");
  $stmt->close();
  $return = '{ "success":"success" }';
  echo $return;





$stmt->close();


}

function checkifUsernameAlreadyOccupate($username)
{


  // COntrollo che non sia vuoto il valore di $username
  if(!isset($_POST["username_instagram"]))
  {
    return false;
  }

  // prima guardo se per caso c'è un altro utente con quella username, nel caso dico che ho gia inserito
  $query = "SELECT * FROM REGISTERED_USERS WHERE USERNAME = ? ";
  global $conn;
  $stmt = $conn->prepare($query);
  $stmt->bind_param("s",$username);
  $stmt->execute();

  $stmt->store_result();

  if ($stmt->num_rows == 1 )
  {
    $stmt->close();
    // Se sono qui allora lo username passato e' gia preso da un altra persona
    return false;
  }else{
    $stmt->close();
    return true;
  }
}




?>
