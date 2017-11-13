<?php
$con = mysql_connect("localhost","root","1234");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }

mysql_select_db("yiibaidb", $con);

$result = mysql_query("select * from items");

echo "<table border='1'>
<tr>
<th>id</th>
<th>item_no</th>
</tr>";

while($row = mysql_fetch_array($result))
  {
  echo "<tr>";
  echo "<td>" . $row['id'] . "</td>";
  echo "<td>" . $row['item_no'] . "</td>";
  echo "</tr>";
  }
echo "</table>";

mysql_close($con);
?>
