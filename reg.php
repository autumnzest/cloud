<?php
if(!isset($_POST['submit'])){
    exit('エラー!');
}
$username = $_POST['username'];
$password = $_POST['password'];
//注册信息判断
if(!preg_match('/^[\w\x80-\xff]{3,15}$/', $username)){
    exit('error：username is unavailiable。<a href="javascript:history.back(-1);">return</a>');
}
if(strlen($password) < 4){
    exit('error：password is too short。<a href="javascript:history.back(-1);">return</a>');
}
//包含数据库连接文件
include('conn.php');
//检测用户名是否已经存在
$check_query = mysql_query("select user_id from user_list where user_name='$username' limit 1");
if(mysql_fetch_array($check_query)){
    echo 'error：username ',$username,' is used。<a href="javascript:history.back(-1);">返回</a>';
    exit;
}
//写入数据
$password = MD5($password);
$regdate = date("Y-m-d",time());
$sql = "INSERT INTO user_list(user_name,password,create_date)VALUES('$username','$password',$regdate)";
if(mysql_query($sql,$conn)){
    exit('registered！click <a href="login.html">登録</a>');
} else {
    echo 'sorry！register is failed：',mysql_error(),'<br />';
    echo 'click <a href="javascript:history.back(-1);">戻す</a> ';
}
?>
