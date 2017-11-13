<?php
$username = $_SESSION['user_name'];

//包含数据库连接文件
include('conn.php');
//检测用户名及密码是否正确
$result = mysql_query("select * from host_list ");

echo "<table border='1'>
<tr>
<th>host_id</th>
<th>host_name</th>
<th>available</th>
<th>total</th>
<th>used</th>
</tr>";
echo '<a href="hostadd.html">hostregister</a>';

while($row = mysql_fetch_array($result))
  {
  echo "<tr>";
  echo "<td>" . $row['host_id'] . "</td>";
  echo "<td>" . $row['host_name'] . "</td>";
  echo "<td>" . $row['available'] . "</td>";
  echo "<td>" . $row['total'] . "</td>";
  echo "<td>" . $row['used'] . "</td>";
  echo "</tr>";
  }
echo "</table>";
echo '<link rel="stylesheet" type="text/css" href="/css/style.css">';

mysql_close($con);
?>
