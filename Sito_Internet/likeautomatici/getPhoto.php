<?php
require_once('../util/connect.php');

/*
Questo file ermette di ottenere tutte le foto che non hanno ancora un numero definito di like
*/

$max_like = $_GET["max_like"];

//Ottengo la prima tupla a cui mandare il messaggio
$query = "SELECT * FROM  `LIKE_AUTOMATICI` ";
$stmt = $conn->prepare($query);
$stmt->execute();
$result = get_result($stmt);
$myArray = array();
foreach ($result as $row)
{
  // ottengo tutte le persone che hanno messo like a quella foto.
  $USERS_LIKED = $row["USERS_LIKED"];

  //Splitto questo campo dai ";"
  $USERS_LIKED_SPLITTED = explode(";", $USERS_LIKED);

  // Ottengo il numero delle persone che hanno messo like alla foto
  $COUNT_USERS_LIKED = count($USERS_LIKED_SPLITTED);

// COntrollo quanti like ha la foto e se ne ha meno di quanto gli ho impostato allora mando al file python la tupla
// In modo da mandare altri like
  if($COUNT_USERS_LIKED < intval($max_like) )
  {
    $tempArray = $row;
    array_push($myArray, $tempArray);

  }


}

echo json_encode($myArray);







?>
