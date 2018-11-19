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

// Faccio una query in cui mi faccio tornare la data fine abbonamento, nel caso sia minore di ora allora imposto:
// TEMPO_FINE_ISCRIZIONE = ora + secondi che ho passato come parametro in post
// Altrimenti TEMPO_FINE_ISCRIZIONE = TEMPO_FINE_ISCRIZIONE(che torna dalla query) + secondi che passo come parametro in post
$query = "SELECT `TEMPO_FINE_ISCRIZIONE` FROM `REGISTERED_USERS` WHERE `USERNAME` = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("s",$username)or die("Errore nella bind_param");
$stmt->execute();
$result = get_result($stmt);
$row = json_decode(json_encode($result[0]), FALSE);;

$TEMPO_FINE_ISCRIZIONE = $row->TEMPO_FINE_ISCRIZIONE;
$tempo_ora = time();
if($tempo_ora > $TEMPO_FINE_ISCRIZIONE)
{
  $TEMPO_FINE_ISCRIZIONE = $tempo_fine_iscrizione + $tempo_ora;
}else {
  $TEMPO_FINE_ISCRIZIONE = $TEMPO_FINE_ISCRIZIONE + $tempo_fine_iscrizione;
}
$stmt->close();
echo "TEMPO FINE ISCRIZIONE DA SETTARE ".$TEMPO_FINE_ISCRIZIONE;




$query = "UPDATE `REGISTERED_USERS` SET `SCRIPT_ACTIVE` = 1 ,`TEMPO_FINE_ISCRIZIONE` = ?, `DEVE_PAGARE` = 0 WHERE `REGISTERED_USERS`.`USERNAME` = ? ";
$stmt = $conn->prepare($query)or die("Errore nella prepare");
$stmt->bind_param("is",$TEMPO_FINE_ISCRIZIONE,$username)or die("Errore nella bind_param");
$stmt->execute()or die("Errore nella execute");


?>