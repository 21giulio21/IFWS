<?php

require_once('../util/connect.php');


$email_user = $_POST["email"];
$password_user = $_POST["password"];
$username_instagram = $_POST["username_instagram"];


// prima guardo se per caso c'è un altro utente con quella mail, nel caso dico che ho gia inserito
$query = "SELECT * FROM `REGISTERED_USERS` WHERE `EMAIL` = ? ";
$stmt = $conn->prepare($query);
$stmt->bind_param("s",$email_user);
$stmt->execute();
if($stmt->num_rows == 1  )
{
// Se sono qui allora ho gia inserito un utente con quell'username
$return = '{ "success":"failed", "reason":"Email already in use" }';
echo $return;

}else{


  $query = "INSERT INTO `my_getfollowersoninstagram`.`REGISTERED_USERS` (`ID`, `USERNAME`, `COOKIES`, `SCRIPT_ACTIVE`, `FOLLOW_UNFOLLOW`, `USERS_FOLLOWED`, `EMAIL`, `PASSWORD_SITE`, `PASSWORD_INSTAGRAM`, `DELTA_T`, `SECONDI_ULTIMA_RICHIESTA`, `NUMBER_REQUESTS_DONE`, `TEMPO_ATTESA_BLOCCO`) VALUES ('', ? , '', '0', '1', '', ? , ? , '', '', '0', '0', '0');";
  $stmt = $conn->prepare($query);
  $stmt->bind_param("sss",$username_instagram,$email_user,$password_user);
  $stmt->execute();
  $return = '{ "success":"success" }';
  echo $return;


}




?>
