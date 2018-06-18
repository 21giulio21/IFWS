<?php


$servername = "localhost";
$username = "getfollowersoninstagram";
$password = "";
$dbname = "my_getfollowersoninstagram";

$email_user = $_POST["email"];
$password_user = $_POST["password"];
$username_instagram = $_POST["username_instagram"];

$conn = new mysqli($servername, $username, $password, $dbname);

// prima guardo se per caso c'è un altro utente con quella mail, nel caso dico che ho gia inserito
$query = "SELECT * FROM `REGISTERED_USERS` WHERE `EMAIL` = '$email_user' ";
$result = $conn->query($query) or die ("queru");
if($result->num_rows > 0 )
{
// Se sono qui allora ho gia inserito un utente con quell'username
$return = '{ "success":"failed", "reason":"Email already in use" }';
echo $return;

}else{


  $query = "INSERT INTO `my_getfollowersoninstagram`.`REGISTERED_USERS` (`ID`, `USERNAME`, `COOKIES`, `SCRIPT_ACTIVE`, `FOLLOW_UNFOLLOW`, `USERS_FOLLOWED`, `EMAIL`, `PASSWORD_SITE`, `PASSWORD_INSTAGRAM`, `DELTA_T`, `SECONDI_ULTIMA_RICHIESTA`, `NUMBER_REQUESTS_DONE`, `TEMPO_ATTESA_BLOCCO`) VALUES ('', '{$username_instagram}', '', '0', '1', '', '{$email_user}', '{$password_user}', '', '', '0', '0', '0');";
  $result = $conn->query($query) or die ("queru");
  $return = '{ "success":"success" }';
  echo $return;


}




?>
