<?php



function login($username,$password)
{
  $ch = curl_init();

  curl_setopt($ch, CURLOPT_URL, "https://www.instagram.com/accounts/login/ajax/");
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
  curl_setopt($ch, CURLOPT_POSTFIELDS, "username=".$username."&password=".$password."&queryParams=%7B%7D");
  curl_setopt($ch, CURLOPT_POST, 1);
  curl_setopt($ch, CURLOPT_ENCODING, 'gzip, deflate');

  $headers = array();
  $headers[] = "Cookie: ig_cb=1";
  $headers[] = "Origin: https://www.instagram.com";
  $headers[] = "Accept-Encoding: gzip, deflate, br";
  $headers[] = "Accept-Language: it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7";
  $headers[] = "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/67.0.3396.99 Chrome/67.0.3396.99 Safari/537.36";
  $headers[] = "X-Requested-With: XMLHttpRequest";
  $headers[] = "X-Csrftoken: C4f4FvL3X1vuYFMV1R5Y6QFeVUnlKhBo";
  $headers[] = "Pragma: no-cache";
  $headers[] = "X-Instagram-Ajax: dad8d866382b";
  $headers[] = "Content-Type: application/x-www-form-urlencoded";
  $headers[] = "Accept: */*";
  $headers[] = "Cache-Control: no-cache";
  $headers[] = "Authority: www.instagram.com";
  $headers[] = "Referer: https://www.instagram.com/accounts/login/";
  curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

  $result = curl_exec($ch);

  echo "<script></script>";

  if (curl_errno($ch)) {
      echo 'Error:' . curl_error($ch);
  }
  curl_close ($ch);
/*
Da qui parsiamo il ritorno della curl.
Nel caso sia andata a buon fine: {"authenticated": true, "user": true, "userId": "819693525", "oneTapPrompt": false, "status": "ok"}
Quindi cerco di capire quando authenticated è true.
*/

  $obj = json_decode($result);

/*
La variabile $authenticated è 1 solamente se "authenticated": true altrimenti non esce nulla scritto.
*/

  $authenticated = $obj->{'authenticated'};
  $return = array();
  if($authenticated == '1')
  {
    // Torno success perche le credenziali sono corrette.
    $return["success"] = "success";
    return json_encode($return);

  }else{

    $return["success"] = "success";
    $return["reason"] = "Credentials not valid";

    return json_encode($return);

  }



}





?>
