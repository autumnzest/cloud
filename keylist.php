<?php
$username = $_SESSION['user_name'];

//包含数据库连接文件
include('conn.php');
//检测用户名及密码是否正确
$result = mysql_query("select * from ssh_list");

echo "<table border='1'>
<tr>
<th>ssh_id</th>
<th>key_name</th>
<th>location</th>
<th>ssh_key</th>
<th>created_at</th>
<th>updated_at</th>
</tr>";

while($row = mysql_fetch_array($result))
  {
  echo "<tr>";
  echo "<td>" . $row['ssh_id'] . "</td>";
  echo "<td>" . $row['key_name'] . "</td>";
  echo "<td>" . $row['location'] . "</td>";
  echo "<td>" . $row['ssh_key'] . "</td>";
  echo "<td>" . $row['created_at'] . "</td>";
  echo "<td>" . $row['updated_at'] . "</td>";
  echo "</tr>";
  }
echo "</table>";

echo '<a href="keyadd.html">keyadd</a>';
echo '<link rel="stylesheet" type="text/css" href="/css/style.css">';

mysql_close($con);
?>
