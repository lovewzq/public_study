<?php
$con = mysql_connect("localhost","root","root");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }

// Create table in my_db database
mysql_select_db("study_first", $con);
$sql = "CREATE TABLE Persons 
(
user_Name varchar(15),
user_Passwd int,
)";
mysql_query($sql,$con);

mysql_close($con);
?>