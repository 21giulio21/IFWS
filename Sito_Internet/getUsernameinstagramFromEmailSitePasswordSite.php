
<?php

require_once('util/connect.php');

$email= $_POST["email"];
$password_site = $_POST["password_site"];
echo "pass".$password_site;

// prima guardo se per caso c'è un altro utente con quella mail, nel caso dico che ho gia inserito
$query = "SELECT * FROM `REGISTERED_USERS` WHERE `EMAIL` = ? AND `PASSWORD_SITE` = ? ";

$stmt = $conn->prepare($query) or die("Errore nella prepare");
$stmt->bind_param("ss", $email,$password_site) or die("Errore nella bind_param");
$stmt->execute() or die("Errore nella execute");
$result = $stmt->get_result() or die("Errore nella get_result");


$stmt->store_result();

printf("Number of rows: %d.\n", $stmt->num_rows);

$myArray = array();
while ($row = $result->fetch_object())
{
  $tempArray = $row;
  array_push($myArray, $tempArray);
}
echo json_encode($myArray);


?>
