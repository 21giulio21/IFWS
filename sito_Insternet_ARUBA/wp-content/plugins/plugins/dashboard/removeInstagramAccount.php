<?php
session_start();
function removeinstagramAccount($username)
{
  if(isset($username))
  {
    //Devo cancellare quello username dal database
    $target_address = "http://2.230.243.113/instagram/app/removeInstagramAccount.php";
    $parametri = array();
    $parametri["username"] = $username;
    curl_request_remove_account($target_address, $parametri);
  }
}

function curl_request_remove_account($target_url, array $arguments){

  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL,$target_url);
  curl_setopt($ch, CURLOPT_POST, 1);
  curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($arguments));

  // receive server response ...
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  $server_output = curl_exec ($ch)or die("Errore nella curl_exec");
  curl_close ($ch);
  return $server_output;

}

?>
