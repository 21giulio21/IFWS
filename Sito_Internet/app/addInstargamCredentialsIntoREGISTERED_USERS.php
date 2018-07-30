<?php

require_once('../util/connect.php');

/*
Questo file php permette di inserire un account instagram una volta arrivati sulla
tabella personale dell'utente dal sito internet

*/



if(!isset($_POST["USERNAME"]) || !isset($_POST["PASSWORD_INSTAGRAM"]) || !isset($_POST["EMAIL"]) )
{
  $return = '{ "success":"failed", "reason":"POST data not valid" }';
  echo $return;
  return;
}


$username_instagram = $_POST["USERNAME"];
$password_instagram = $_POST["PASSWORD_INSTAGRAM"];
$email = $_POST["EMAIL"];



//Questa variabile contiene il secondo in cui viene chiamata la pagina,
//in maniera tale che una volta passati 3 giorni devo far pagare l'utente.
$secondi = time();

// Controllo che l'username che l'utente vuole inserire non sia gia all'interno del database
// prima guardo se per caso c'è un altro utente con quella username, nel caso dico che ho gia inserito
$query = "SELECT * FROM `REGISTERED_USERS` WHERE `USERNAME` = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("s",$username_instagram);
$stmt->execute();
$stmt->store_result();

if ($stmt->num_rows == 1 )
{
// Se sono qui allora lo username passato e' gia preso da un altra persona

  $return = '{ "success":"failed", "reason":"Username already in use" }';
  echo $return;

}else{

  // Inserisco le credenziali dell'utente
  $query = "
  INSERT INTO `REGISTERED_USERS`
  (`ID`, `USERNAME`, `COOKIES`, `SCRIPT_ACTIVE`, `FOLLOW_UNFOLLOW`, `USERS_FOLLOWED`,
   `EMAIL`, `PASSWORD_INSTAGRAM`, `DELTA_T`, `SECONDI_ULTIMA_RICHIESTA`, `NUMBER_REQUESTS_DONE`,
   `TEMPO_ATTESA_BLOCCO`, `PASSWORD_ERRATA`, `TARGET`, `COMMENTA`, `SET_LIKE`, `DEVE_PAGARE`,
    `TEMPO_ISCRIZIONE`) VALUES
    ('', ? , '', '0', '1', '', ? , ? , '200', '0', '0', '0', '0', '', '0', '0', '0', ? );";
  $stmt = $conn->prepare($query)or die("Errore nella prepare");
  $stmt->bind_param("ssss",$username_instagram,$email,$password_instagram,$secondi)or die("Errore nella bind_param");
  $stmt->execute()or die("Errore nella execute nel file addInstagra... riga 58");
  $stmt->store_result()or die("Errore nella store_result");

  $return = '{ "success":"success" }';

  echo $return;


}






?>
