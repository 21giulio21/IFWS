
<?php

require_once('util/connect.php');
/////////////

//// TODO MEGLIO

////////


// prima guardo se per caso c'è un altro utente con quella mail, nel caso dico che ho gia inserito
$query = "SELECT * FROM `REGISTERED_USERS` WHERE `EMAIL` = ? AND `PASSWORD_SITE` = ? ";

$stmt = $conn->prepare($query) or die("Errore nella prepare");
$stmt->bind_param("ss", $email,$password_site) or die("Errore nella bind_param");

$email= $_POST["email"];
$password_site = "21giulio21@gmail.com";

$stmt->execute() or die("Errore nella execute");
$result = $stmt->get_result() or die("Errore nella get_result");



$myArray = array();
while ($row = $result->fetch_object())
{
  $tempArray = $row;
  array_push($myArray, $tempArray);
}
echo json_encode($myArray);


?>
