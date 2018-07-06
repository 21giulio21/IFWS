<?php


require_once('../util/connect.php');


$username= $_POST["username"];


// prima guardo se per caso c'è un altro utente con quella mail, nel caso dico che ho gia inserito
$query = "SELECT * FROM `REGISTERED_USERS` WHERE `USERNAME` = '${username}' ";
$result = $conn->query($query) or die ("Query non funzionante");
$myArray = array();
while ($row = $result->fetch_object())
{
                $tempArray = $row;
                array_push($myArray, $tempArray);
            }
        echo json_encode($myArray);

?>
