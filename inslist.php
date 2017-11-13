<?php
$username = $_SESSION['user_name'];
$keyword = $_POST['keyword'];

//包含数据库连接文件
include('conn.php');
//检测用户名及密码是否正确
$result = mysql_query("select * from instance_list "
        . "where ins_id like '%$keyword%' "
        . "or ins_uuid like '%$keyword%'"
        . "or ins_name like '%$keyword%'"
        . "or ip_addr like '%$keyword%'"
        . "or host_id like '%$keyword%'"
        . "or autostart like '%$keyword%'"
        . "or user_id like '%$keyword%'"
        . "or ssh_id like '%$keyword%'"
        . "or ram like '%$keyword%'"
        . "or vcpus like '%$keyword%'"
        . "or status like '%$keyword%'"
        . "or created_at like '%$keyword%'"
        . "or updated_at like '%$keyword%'"	
	. ";");

echo '<link rel="stylesheet" type="text/css" href="/css/style.css">';
echo "<table border='1'>
<tr>
<th>ins_id</th>
<th>ins_uuid</th>
<th>ins_name</th>
<th>ip_addr</th>
<th>host_id</th>
<th>autostart</th>
<th>user_id</th>
<th>ssh_id</th>
<th>ram</th>
<th>vcpus</th>
<th>status</th>
<th>created_at</th>
<th>updated_at</th>
</tr>";

echo '<div>
<legend>inslist</legend>
<form name="InsForm" method="post" action="inslist.php">
<input id="keyword" name="keyword" type="text" class="input" />
<input type="submit" name="submit" value=" search "/><br/>
</form>
</div>';

while($row = mysql_fetch_array($result))
  {
  echo "<tr>";
  echo "<td>" . $row['ins_id'] . "</td>";
  echo "<td>" . $row['ins_uuid'] . "</td>";
  echo "<td>" . $row['ins_name'] . "</td>";
  echo "<td>" . $row['ip_addr'] . "</td>";
  echo "<td>" . $row['host_id'] . "</td>";
  echo "<td>" . $row['autostart'] . "</td>";
  echo "<td>" . $row['user_id'] . "</td>";
  echo "<td>" . $row['ssh_id'] . "</td>";
  echo "<td>" . $row['ram'] . "</td>";
  echo "<td>" . $row['vcpus'] . "</td>";
  echo "<td>" . $row['status'] . "</td>";
  echo "<td>" . $row['created_at'] . "</td>";
  echo "<td>" . $row['updated_at'] . "</td>";
  echo "</tr>";
  }
echo "</table>";

echo '<a href="insadd.html">insadd</a>';

mysql_close($con);
?>
