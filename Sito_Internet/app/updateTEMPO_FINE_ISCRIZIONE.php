<?php


require_once('../util/connect.php');

if( !isset($_POST["USERNAME"]) || !isset($_POST["TEMPO_FINE_ISCRIZIONE"]) )
{
  $return = '{ "success":"failed", "reason":"POST data not valid" }';
  echo $return;
  return;
}



$username = $_POST["USERNAME"];
$tempo_fine_iscrizione = $_POST["TEMPO_FINE_ISCRIZIONE"];


$query = "UPDATE `REGISTERED_USERS` SET `TEMPO_FINE_ISCRIZIONE` = ? WHERE `REGISTERED_USERS`.`USERNAME` = ? ";
echo "Dati ricevuti: ".$username.$tempo_fine_iscrizione;
$stmt = $conn->prepare($query)or die("Errore nella prepare");
$stmt->bind_param("is",$tempo_fine_iscrizione,$username)or die("Errore nella bind_param");
$stmt->execute()or die("Errore nella execute");


?>
