<?php
session_star();


function confirmEmailAddress()
{

//Prendo come input i parametri della pagina precedente e creo un codice da inserire che deve essere convalidato via mail.
print("SOno nella funzione confirmEmailAddress");
$password =  $_SESSION["password"];
$email = $_SESSION["email"];

echo $email . $password;



}








add_shortcode( 'confirmEmailAddress', 'confirmEmailAddress' );


?>
