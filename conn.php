<?php
/*****************************
*数据库连接
*****************************/
$conn = @mysql_connect("localhost","root","1234");
if (!$conn){
    die("データベース接続できない：" . mysql_error());
}
mysql_select_db("cloud", $conn);
//字符转换，读库
//mysql_query("set character set 'gbk'");
//写库
//mysql_query("set names 'gbk'");
?>
