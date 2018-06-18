<?php


$servername = "localhost";
$username = "getfollowersoninstagram";
$password = "";
$dbname = "my_getfollowersoninstagram";
$conn = new mysqli($servername, $username, $password, $dbname);

$username= $_POST["username"];


// prima guardo se per caso c'è un altro utente con quella mail, nel caso dico che ho gia inserito
$query = "SELECT * FROM `REGISTERED_USERS` WHERE `USERNAME` = '${username}' ";
$result = $conn->query($query) or die ("queru");
$myArray = array();
while ($row = $result->fetch_object())
{
                $tempArray = $row;
                array_push($myArray, $tempArray);
            }
        echo json_encode($myArray);

?>

?>
