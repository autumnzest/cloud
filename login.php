<?php
session_start();

//注销登录
if($_GET['action'] == "logout"){
    unset($_SESSION['userid']);
    unset($_SESSION['user_name']);
    echo 'logout success！click <a href="login.html">登録</a>';
    exit;
}

//登录
if(!isset($_POST['submit'])){
    exit('error!<a href="javascript:history.back(-1);">戻す</a>');
}
$username = htmlspecialchars($_POST['username']);
$password = MD5($_POST['password']);

//包含数据库连接文件
include('conn.php');
//检测用户名及密码是否正确
$check_query = mysql_query("select user_id from user_list where user_name='$username' and password='$password' 
limit 1");
if($result = mysql_fetch_array($check_query)){
    //登录成功
    $_SESSION['username'] = $username;
    $_SESSION['userid'] = $result['user_id'];
    echo 'Welcome! ' ,$username , '<br/>';
    echo 'click <a href="login.php?action=logout">logout</a><br />';
    echo 'click <a href="hostlist.php">hostlist</a><br />';	
    echo 'click <a href="inslist.php">inslist</a><br />';
    echo 'click <a href="keylist.php">keylist</a><br />';
	exit;
} else {
    exit('cant login in！click <a href="javascript:history.back(-1);">戻す</a> ');
}
?>
