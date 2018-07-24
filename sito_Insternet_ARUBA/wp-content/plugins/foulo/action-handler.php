<?php

if(isset($_POST["action"], $_POST["parameters"])) {

  switch ($_POST["action"]) {
    case 'toggle-bot':
      $target_address = "http://2.230.243.113/instagram/app/updateScriptActive.php";
      print_r(curl_request($target_address, $_POST["parameters"]));
      break;

    default:
      break;
  }

}




function curl_request($target_url, array $arguments){

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
