<?php
if(!isset($_POST['submit'])){
    exit('エラー!');
}
$keyname = $_POST['keyname'];
$regdate = date("Y-m-d",time());

//注册信息判断
if(!preg_match('/^[\w\x80-\xff]{3,15}$/', $keyname)){
    exit('error：keyname is unavailiable。<a href="javascript:history.back(-1);">return</a>');
}
//包含数据库连接文件
include('conn.php');
//检测用户名是否已经存在
$check_query = mysql_query("select ssh_id from ssh_list where key_name='$keyname' limit 1");
if(mysql_fetch_array($check_query)){
    echo 'error：keyname ',$keyname,' is used。<a href="javascript:history.back(-1);">return</a>';
    exit;
}
//写入数据
$sql = "INSERT INTO ssh_list(key_name,created_at)VALUES('$keyname','$regdate')";
if(mysql_query($sql,$conn)){
    exit('registered！click <a href="keylist.php">keylist</a>');
} else {
    echo 'sorry！register is failed：',mysql_error(),'<br />';
    echo 'click <a href="javascript:history.back(-1);">戻す</a> ';
}
?>
