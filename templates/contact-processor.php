<?php
print_r($_POST);
die;
if(!empty($_POST['SUBMIT'])){
  $name = $_POST['name'];
  $emailAdress = $_POST['email'];
  $phoneNumber = $_POST['phone'];
  $message = $_POST['message'];

  $mailTo = "contact@site4u.ca";
  $headers = "From: ".$name." Number: ".$phoneNumber;
  $txt = "You have received an email from: ".$emailAdress.". \n\n".$message;



  mail($mailTo, $headers, $txt);
  header("Location: /formSent");
}

?>
