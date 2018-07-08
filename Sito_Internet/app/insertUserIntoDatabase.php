<?php

require_once('../util/connect.php');
global $conn;
/*
Questa pagina viene chiamata nel momento in cui volgio registrare un utente
In particolare passo qui i dati che devono essere inseriti nel database REGIATRED_USERS

*/

$email_user = $_POST["email"];
$password_user = $_POST["password"];
$username_instagram = $_POST["username_instagram"];

// COntrollo che lp username non sia preso da altree persone
if(!checkifUsernameAlreadyOccupate($username_instagram))
{
  $return = '{ "success":"failed", "reason":"Email already in use" }';
  echo $return;
  return;
}


// prima guardo se per caso c'è un altro utente con quella mail, nel caso dico che ho gia inserito
$query = "SELECT * FROM REGISTERED_USERS WHERE EMAIL = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("s",$email_user);
$stmt->execute();
$stmt->close();
if($stmt->num_rows == 1  )
{
// Se sono qui allora ho gia inserito un utente con quell'username
$return = '{ "success":"failed", "reason":"Email already in use" }';
echo $return;

}else{


  //$query = "INSERT INTO REGISTERED_USERS (ID, USERNAME, COOKIES, SCRIPT_ACTIVE, FOLLOW_UNFOLLOW, USERS_FOLLOWED, EMAIL, PASSWORD_SITE, PASSWORD_INSTAGRAM,DELTA_T, SECONDI_ULTIMA_RICHIESTA, NUMBER_REQUESTS_DONE, TEMPO_ATTESA_BLOCCO, URL_IMMAGINE_PROFILO, PROCESSING, PASSWORD_ERRATA, TARGET,COMMENTA) VALUES ('', 'gggggg', '', '0', '1', '', 'gggggg', 'erggggg', '', '100', '0', '0', '0', '', '0', '0', '', '0')";
  $query = "INSERT INTO `my_getfollowersoninstagram`.`REGISTERED_USERS` (`ID`, `USERNAME`, `COOKIES`, `SCRIPT_ACTIVE`, `FOLLOW_UNFOLLOW`, `USERS_FOLLOWED`, `EMAIL`, `PASSWORD_SITE`, `PASSWORD_INSTAGRAM`, `DELTA_T`, `SECONDI_ULTIMA_RICHIESTA`, `NUMBER_REQUESTS_DONE`, `TEMPO_ATTESA_BLOCCO`, `URL_IMMAGINE_PROFILO`, `PROCESSING`, `PASSWORD_ERRATA`, `TARGET`, `COMMENTA`) VALUES ('', ? , '', '0', '1', '', ? , ? , '', '100', '0', '0', '0', '', '0', '0', '', '0');";
  $stmt = $conn->prepare($query);
  $stmt->bind_param("sss",$username_instagram,$email_user,$password_user);
  $stmt->execute()or die("Errore nella execute");

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
