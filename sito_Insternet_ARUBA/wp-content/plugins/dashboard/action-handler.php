<?php
//Serve averla perche quando mando al mio server i dati devo mandare anche la mail.
session_start();

//includo il file login.php per far si che l'utente prima di essere inserito nel mio DB abbia le credenziali corrette.
require_once("login.php");

if(isset($_POST["action"], $_POST["parameters"])) {

  switch ($_POST["action"]) {
    case 'toggle-bot':
      $target_address = "http://www.elenarosina.com/instatrack/app/updateScriptActive.php";
      print_r(curl_request($target_address, $_POST["parameters"]));
      break;

    case 'toggle-comments':
      $target_address = "http://www.elenarosina.com/instatrack/app/updateCommenta.php";
      print_r(curl_request($target_address, $_POST["parameters"]));
      break;

    case 'toggle-likes':
      $target_address = "http://www.elenarosina.com/instatrack/app/updateLike.php";
      print_r(curl_request($target_address, $_POST["parameters"]));
      break;
    case "CHOOSE-CATEGORY":
    $target_address = "http://www.elenarosina.com/instatrack/app/updateCategoryFromUsername.php";
    print_r(curl_request($target_address, $_POST["parameters"]));

    break;
    case 'ADD_INSTAGRAM_ACCOUNT':
    /* TOLGI IL COMMENTO A QUESTO CODICE SE VUOI PRIMA FARE IL LOGIN SU INSTAGRAM PER CONTROLLARE LE CREDENZIALI


      //Faccio per prima il login per vedere se i dati dell nuovo utente sono corretti, poi lo inserisco dentro al mio server


      $response_login = json_decode(login($_POST['parameters']['USERNAME'],$_POST['parameters']['PASSWORD_INSTAGRAM']));
      // se login torna: '{ "success":"failed", "reason":"Username already in use" }' allora non devo proseguire
      if ($response_login->success == "success")
      {
        // allora inserisco l'utente nel mio database
        $target_address = "http://www.elenarosina.com/instatrack/app/addInstargamCredentialsIntoREGISTERED_USERS.php";
        $_POST['parameters']['EMAIL']  = $_SESSION["email"] ;
        curl_request($target_address, $_POST["parameters"]);
        break;
      }*/

      // inserisco l'utente forzato senza login
      $target_address = "http://www.elenarosina.com/instatrack/app/addInstargamCredentialsIntoREGISTERED_USERS.php";
      $_POST['parameters']['EMAIL']  = $_SESSION["email"] ;
      curl_request($target_address, $_POST["parameters"]);


      break;
    case 'RENEW-SUBSCRIPTION':
      $target_url = "http://www.elenarosina.com/instatrack/app/updateTEMPO_FINE_ISCRIZIONE.php";
      $return = curl_request($target_url,$_POST['parameters']);
      echo"console.log($return)";
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
