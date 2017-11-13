<?php
if(!isset($_POST['submit'])){
    exit('エラー!');
}
$ins_name = $_POST['ins_name'];
$ip_addr = $_POST['ip_addr'];
$ram = $_POST['ram'];
$vcpus = $_POST['vcpus'];
$regdate = date("Y-m-d",time());
//注册信息判断
if(!preg_match('/^[\w\x80-\xff]{3,15}$/', $ins_name)){
    exit('error：hostname is unavailiable。<a href="javascript:history.back(-1);">return</a>');
}
if(strlen($ip_addr) < 0){
    exit('error：space is too small。<a href="javascript:history.back(-1);">return</a>');
}
//包含数据库连接文件
include('conn.php');
//检测用户名是否已经存在
$check_query = mysql_query("select ins_id from instance_list where ins_name='$ins_name' limit 1");
if(mysql_fetch_array($check_query)){
    echo 'error：ins_name ',$ins_name,' is used。<a href="javascript:history.back(-1);">return</a>';
    exit;
}
//写入数据
$sql = "INSERT INTO instance_list(ins_uuid,ins_name,ip_addr,ram,vcpus,status,created_at)VALUES('111','$ins_name','$ip_addr','$ram','$vcpus','1','$regdate')";
if(mysql_query($sql,$conn)){
    exit('registered！click <a href="inslist.php">inslist</a>');
} else {
    echo 'sorry！register is failed：',mysql_error(),'<br />';
    echo 'click <a href="javascript:history.back(-1);">戻す</a> ';
}
?>
