<?php
if(!isset($_POST['submit'])){
    exit('エラー!');
}
$hostname = $_POST['hostname'];
$total = $_POST['total'];
//注册信息判断
if(!preg_match('/^[\w\x80-\xff]{3,15}$/', $hostname)){
    exit('error：hostname is unavailiable。<a href="javascript:history.back(-1);">return</a>');
}
if(strlen($total) < 0){
    exit('error：space is too small。<a href="javascript:history.back(-1);">return</a>');
}
//包含数据库连接文件
include('conn.php');
//检测用户名是否已经存在
$check_query = mysql_query("select user_name from host_list where host_name='$hostname' limit 1");
if(mysql_fetch_array($check_query)){
    echo 'error：hostname ',$hostname,' is used。<a href="javascript:history.back(-1);">return</a>';
    exit;
}
//写入数据
$sql = "INSERT INTO host_list(host_name,total)VALUES('$hostname','$total')";
if(mysql_query($sql,$conn)){
    exit('registered！click <a href="hostlist.php">hostlist</a>');
} else {
    echo 'sorry！register is failed：',mysql_error(),'<br />';
    echo 'click <a href="javascript:history.back(-1);">戻す</a> ';
}
?>
