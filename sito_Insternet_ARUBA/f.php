<?php

login("vika.giulio","21giulio21");

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
  curl_setopt($ch,CURLOPT_HEADER,1);

  $result = curl_exec($ch);

  preg_match_all('/^Set-Cookie:s*([^;]*)/mi', $result, $matches);
  $cookies = array();
  foreach($matches[1] as $item) {
    parse_str($item, $cookie);
    $cookies = array_merge($cookies, $cookie);
  }
  foreach ($cookies as $key => $value) {
    echo "Key: $key; Value: $value";
}

  if (curl_errno($ch)) {
      echo 'Error:' . curl_error($ch);
  }
  curl_close ($ch);



}





?>
