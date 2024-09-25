---
title: mysql+php+html实现学生管理系统
date: 2024-07-30 17:30:00
tags: 其他
---
## 前言

本文使用Mysql+php+html实现一个简单的学生管理系统，实现了登陆，注册，总览学生信息，添加学生，查询特定的学生，删除指定的学生等功能。并且本文仅用来学习就够了，因为在实际开发中都会使用框架比如前端的vue.js，后端用的springboot，使用这些框架能大幅提高开发效率，避免重复造轮子，所以不必要进行太过深入地了解这些技术。🙂

### 开发平台

- Phpstudy/PhpEnv：我个人比较推荐[phpEnv-专业优雅强大的php集成环境](https://www.phpenv.cn/)，毕竟Phpstudy太老了，PhpEnv界面操作简单，集成度高，免去配置Mysql数据库，Apache服务器的繁琐操作，直接就能使用。
- Visual studio code：写代码的编辑器，你用自己喜欢的也行。
- DataGrip:数据库的GUI管理工具，可以用图形化界面编写sql语句。

### 版本要求

想要复刻我的代码，使用的软件版本尽量跟我开发的时候写的保持一致，不同的版本会导致**兼容性的问题导致报错**

- Mysql:5.5.53
- php:5.5.38
- apache:不限

> 文章编写都是采用GBK编码，这个要注意

## 功能展示

功能简要来说就是实现了最基本的增删改查

### 主页面

![image-20240730164322529](https://cdn.jsdelivr.net/gh/kashima19960/img@master/Mysql%E5%AD%A6%E7%94%9F%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F/image-20240730164322529.png)

### 查看所有的学生

![image-20240730164517047](https://cdn.jsdelivr.net/gh/kashima19960/img@master/Mysql%E5%AD%A6%E7%94%9F%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F/image-20240730164517047.png)

![image-20240730164525993](https://cdn.jsdelivr.net/gh/kashima19960/img@master/Mysql%E5%AD%A6%E7%94%9F%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F/image-20240730164525993.png)

### 添加学生

![image-20240730164539170](https://cdn.jsdelivr.net/gh/kashima19960/img@master/Mysql%E5%AD%A6%E7%94%9F%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F/image-20240730164539170.png)

### 查找指定的学生

![image-20240730164549702](https://cdn.jsdelivr.net/gh/kashima19960/img@master/Mysql%E5%AD%A6%E7%94%9F%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F/image-20240730164549702.png)

### 登陆功能

![image-20240730164601973](https://cdn.jsdelivr.net/gh/kashima19960/img@master/Mysql%E5%AD%A6%E7%94%9F%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F/image-20240730164601973.png)

## 代码逻辑设计

代码主要分16个代码文件

- add.html
- index.html
- register.html
- search.html
- login.html
- add.php
- delete.php
- login.php
- modify.php
- modify2.php
- overview.php
- register.php
- search.php

### 数据库的相关实现

本学生管理系统一共使用到了两张表

xs表

![image-20240730165819565](https://cdn.jsdelivr.net/gh/kashima19960/img@master/Mysql%E5%AD%A6%E7%94%9F%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F/image-20240730165819565.png)

数据可以参照xs.sql，快速构建表

```sql
DROP TABLE IF EXISTS `xs`;
CREATE TABLE `xs` (
  `学号` char(6) NOT NULL,
  `姓名` char(8) NOT NULL,
  `专业名` char(10) DEFAULT NULL,
  `性别` tinyint(1) NOT NULL DEFAULT '1',
  `出生日期` date NOT NULL,
  `总学分` tinyint(1) DEFAULT NULL,
  `照片` blob,
  `备注` text,
  PRIMARY KEY (`学号`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
--
-- Dumping data for table `xs`
--

LOCK TABLES `xs` WRITE;
INSERT INTO `xs` VALUES ('081101','王休','计算机',1,'1994-02-10',50,NULL,NULL),('081102','程明','计算机',1,'1995-02-01',50,NULL,NULL),('081103','王燕','计算机',0,'1993-10-06',50,NULL,NULL),('081104','韦严平','计算机',1,'1994-08-26',50,NULL,NULL),('081106','李方方','计算机',1,'1994-11-20',50,NULL,NULL),('081107','李明','计算机',1,'1994-05-01',54,NULL,'提前修完\"数据结构\",并获得学分'),('081108','林一帆','计算机',1,'1993-08-05',52,NULL,'已提前修完一门课'),('081109','张强民','计算机',1,'1993-08-11',50,NULL,NULL),('081110','张蔚','计算机',0,'1995-07-22',50,'?','三好生'),('081111','赵琳','计算机',0,'1994-03-18',50,NULL,NULL),('081113','严红','计算机',0,'1993-08-11',48,NULL,'有一门课不及格，待补考'),('081201','王敏','通信工程',1,'1993-06-10',42,NULL,NULL),('081202','王林','通信工程',1,'1993-01-29',40,NULL,'有一门课不及格，待补考'),('081204','马琳琳','通信工程',0,'1993-02-10',40,NULL,NULL),('081206','李计','通信工程',1,'1993-09-20',42,NULL,NULL),('081210','李红庆','通信工程',1,'1993-05-01',42,NULL,'已提前修完一门课，并获得学分'),('081216','孙祥欣','通信工程',1,'1993-03-09',44,NULL,NULL),('081218','孙研','通信工程',1,'1994-10-09',42,NULL,NULL),('081220','吴薇华','通信工程',0,'1994-03-18',42,NULL,NULL),('081221','刘燕敏','通信工程',0,'1993-11-12',42,NULL,NULL),('081241','罗林琳','通信工程',0,'1994-01-30',50,NULL,'转专业学习');
UNLOCK TABLES;

```

user表

![image-20240730165756961](https://cdn.jsdelivr.net/gh/kashima19960/img@master/Mysql%E5%AD%A6%E7%94%9F%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F/image-20240730165756961.png)

数据可以参照user.sql，快速构建表

```sql
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `Host` char(60) COLLATE utf8_bin NOT NULL DEFAULT '',
  `User` char(16) COLLATE utf8_bin NOT NULL DEFAULT '',
  `Password` char(41) CHARACTER SET latin1 COLLATE latin1_bin NOT NULL DEFAULT '',
  `Select_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `Insert_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `Update_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `Delete_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `Create_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `Drop_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `Reload_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `Shutdown_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `Process_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `File_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `Grant_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `References_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `Index_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `Alter_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `Show_db_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `Super_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `Create_tmp_table_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `Lock_tables_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `Execute_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `Repl_slave_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `Repl_client_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `Create_view_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `Show_view_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `Create_routine_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `Alter_routine_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `Create_user_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `Event_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `Trigger_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `Create_tablespace_priv` enum('N','Y') CHARACTER SET utf8 NOT NULL DEFAULT 'N',
  `ssl_type` enum('','ANY','X509','SPECIFIED') CHARACTER SET utf8 NOT NULL DEFAULT '',
  `ssl_cipher` blob NOT NULL,
  `x509_issuer` blob NOT NULL,
  `x509_subject` blob NOT NULL,
  `max_questions` int(11) unsigned NOT NULL DEFAULT '0',
  `max_updates` int(11) unsigned NOT NULL DEFAULT '0',
  `max_connections` int(11) unsigned NOT NULL DEFAULT '0',
  `max_user_connections` int(11) unsigned NOT NULL DEFAULT '0',
  `plugin` char(64) COLLATE utf8_bin DEFAULT '',
  `authentication_string` text COLLATE utf8_bin,
  PRIMARY KEY (`Host`,`User`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Users and global privileges';
```

### 登陆功能实现

Login.html,login.php实验登陆的功能

```html
<-->login.html</-->
<!doctype html>
<html>

<head>
    <meta charset="GBK">
    <title>login</title>
    <style type="text/css">
        /* 设置背景图片和样式 */
        body {
            background-image: url(./¾ýÃû.png); /* 这部分文件名可能有乱码 */
            background-repeat: no-repeat;
            background-size: cover;
            background-attachment: fixed;
        }

        /* 登录框样式 */
        .Login {
            width: 600px;
            height: 350px;
            background: white;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            margin: auto;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 0 5px rgba(3, 60, 245, 0.4);
            background: transparent;
        }

        /* 表单样式 */
        form {
            margin: 25px 140px;
        }

        /* 标题样式 */
        h1 {
            margin-top: 35px;
            text-align: center;
            font-size: 40px;
            color: #000000;
        }

        /* 输入框样式 */
        input {
            width: 220px;
            height: 30px;
            background: transparent;
            margin-top: 30px;
            border: none;
            border-bottom: 1px #a77a27 solid;
            outline: none;
            color: #000000;
            font-size: 17px;
            margin-left: 10px;
        }

        /* 按钮样式 */
        .anniu {
            width: 98px;
            height: 25px;
            border: black;
            margin-top: 50px;
            color: white;
            text-align: center;
            line-height: 30px;
            background-image: linear-gradient(to right, #0849ebf5, #e6134f);
            border-radius: 20px;
            cursor: pointer;
            text-align: center;
        }

        /* 标签样式 */
        label {
            font-size: 18px;
            color: white;
        }
    </style>
</head>

<body>
    <div class="Login">
        <!-- 页面标题 -->
        <h1>µÇÂ½</h1> <!-- 这里的标题可能需要调整为正确的字符编码 -->
        <form action="./login.php" method="POST">
            <!-- 用户名输入框 -->
            <label for="username">
                username<input type="text" name="user" id="usename" placeholder="ÇëÊäÈëÓÃ»§Ãû"> <!-- 占位符文本需要调整为正确的字符编码 -->
            </label>
            <!-- 密码输入框 -->
            <label for="password">
                password<input type="password" name="pwd" id="password" placeholder="ÇëÊäÈëÃÜÂë"> <!-- 占位符文本需要调整为正确的字符编码 -->
            </label>
            <!-- 提交按钮 -->
            <input type="submit" value="µÇÂ½" class="anniu"> <!-- 按钮文本需要调整为正确的字符编码 -->
            <!-- 注册按钮 (暂时注释掉的代码) -->
            <!-- <button type="button" id="btn" value="×¢²á" class="anniu">×¢²á</button> --> <!-- 按钮文本需要调整为正确的字符编码 -->
        </form>
        <script>
            // 绑定注册按钮的点击事件
            var a = document.getElementById("btn");
            a.onclick = function () {
                window.location.href = "register.html"; // 跳转到注册页面
            };
        </script>
    </div>
</body>

</html>

```

```php
//login.php
<?php
// 获取用户输入的用户名和密码
$username = $_POST['username'];
$password = $_POST['password'];

// 连接到 MySQL 数据库
$conn = new mysqli("localhost", "root", "root") or die("连接失败: " . $conn->connect_error);
// 设置数据库连接的字符集为 GBK
$conn->query("set names gbk");

// 从 POST 数据中获取用户名和密码
$username = $_POST['user'];
$password = $_POST['pwd'];

// 查询数据库中的用户信息
$sql = "select * from mysql.user where User='$username' and Password='$password'";
$ret = $conn->query($sql);

// 检查查询结果的行数，判断用户是否存在且密码正确
if ($ret->num_rows == 1) {
    // 用户存在且密码正确，显示成功消息并跳转到主页
    echo "<script>alert(\"恭喜您，登陆成功\")</script>";
    echo "<script>window.location.href='./index.html'</script>";
} else {
    // 用户名或密码错误，显示错误消息并跳转回登录页面
    echo "<script>alert(\"账号或者密码错误，请重新输入\")</script>";
    echo "<script>window.location.href='./login.html'</script>";
}

// 关闭数据库连接
$conn->close();

```

### 添加功能实现

在add.html,add.php实现添加学生的功能

```html
<!-- add.html -->

<!DOCTYPE html>
<html lang="en">

<head>
    <!-- 定义页面的字符集为GBK，并指定文档的语言为英语 -->
    <meta http-equiv="Content-Type" content="text/html; charset=GBK">
    <title>添加学生</title>
    <style>
        /* 定义表单样式 */
        form {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: white;
            line-height: 25px;
        }

        /* 定义表单内标签的样式 */
        form label {
            text-align: center;
        }

        /* 定义提交按钮的样式 */
        form input[type="submit"] {
            background-color: red;
            color: white;
            margin-top: 10px;
            margin-right: 5px;
        }

        /* 定义重置按钮的样式 */
        form input[type="reset"] {
            background-color: blue;
            color: white;
            margin-top: 10px;
            margin-left: 5px;
        }

        /* 定义提交和重置按钮的公共样式 */
        form input[type="submit"],
        form input[type="reset"] {
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        /* 定义单选按钮容器的样式 */
        .radio-container {
            display: flex;
        }

        /* 定义单选按钮标签的样式 */
        .radio-container label {
            margin-right: 10px;
        }

        /* 定义页面背景图片和样式 */
        body {
            background-image: url(./君名.png);
            background-repeat: no-repeat;
            background-size: cover;
            background-attachment: fixed;
        }

        /* 定义通用标签的样式 */
        label {
            font-size: 20px;
            height: 30px;
        }

        /* 定义返回按钮的样式 */
        .return {
            display: inline-block;
            border: 2px solid black;
            border-radius: 20px;
            padding: 5px;
            margin: 5px;
            background-image: linear-gradient(to right, #0849ebf5, #e6134f);
            text-decoration: none;
            font-size: 32px;
            text-align: center;
            color: black;
        }

        /* 定义按钮容器的样式 */
        .button-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
        }

        /* 定义容器内链接的样式 */
        .button-container a {
            display: inline-block;
            border: 2px solid black;
            border-radius: 10px;
            padding: 5px 10px;
            margin: 5px;
            background-image: linear-gradient(to right, #0849ebf5, #e6134f);
            text-decoration: none;
            font-size: 18px;
            text-align: center;
            color: black;
        }
    </style>
</head>

<body>

    <!-- 页面标题 -->
    <h2 style="text-align: center;color: red">添加学生</h2>

    <!-- 表单开始，提交到add.php文件 -->
    <form action="./add.php" method="post">
        <!-- 学号输入框 -->
        <label for="student_id">学号<input type="text" name="id" id="student_id"></label>
        <br>
        <!-- 姓名输入框 -->
        <label for="name">姓名 <input type="text" name="s_name" id="name"></label>
        <br>
        <!-- 专业名输入框 -->
        <label for="major">专业名 <input type="text" name="major_in" id="major"></label>
        <br>
        <!-- 性别选择框 -->
        <div class="radio-container">
            <label><input type="radio" value="1" name="gender" required>男</label>
            <label><input type="radio" value="0" name="gender" required>女</label>
        </div>
        <br>
        <!-- 出生日期输入框 -->
        <label for="date">出生日期<input type="date" id="date" name="date"></label>
        <br>
        <!-- 总学分输入框 -->
        <label for="credit">总学分 <input type="text" id="credit" name="credits"></label>
        <br>
        <!-- 备注输入框 -->
        <label for="note">备注 <input type="text" id="note" name="notes"></label>
        <br>
        <!-- 提交和重置按钮容器 -->
        <div class="button-container">
            <input type="submit" value="提交">
            <input type="reset" value="重置">
        </div>
    </form>
    <!-- 返回按钮容器 -->
    <div class="button-container">
        <a href="./index.html">返回</a>
    </div>

</body>

</html>

```

```php
//add.php

<?php
// 创建与 MySQL 数据库的连接
$conn = new mysqli("localhost", "root", "root", "xscj") or die("连接失败");
// 设置数据库连接的字符集为 GBK
$conn->query("SET NAMES gbk");
?>

<html>

<head>
    <title>添加学生</title>
    <meta http-equiv="Content-Type" content="text/html; charset=GBK">
    <style>
        /* 定义页面背景样式 */
        body {
            background-image: url(./君名.png);
            background-repeat: no-repeat;
            background-size: cover;
            background-attachment: fixed;
        }
    </style>
</head>

<body>
    <?php
    // 获取表单提交的数据
    $id = $_POST['id'];
    $name = $_POST['s_name'];
    $major = $_POST['major_in'];
    $gender = $_POST['gender'];
    $birthday = $_POST['date'];
    $sum_credit = $_POST['credits'];
    $note = $_POST['notes'];
  
    // 检查学号是否为空
    if (empty($id)) {
        // 如果学号为空，显示警告并返回表单页面
        echo ("<script>alert('学号不能为空！')</script>");
        echo ("<script>window.location.href='add.html'</script>");
        $conn->close(); // 关闭数据库连接
    } else {
        // 插入数据到数据库
        $sql = "insert into xs(学号, 姓名, 专业名,性别, 出生日期, 总学分,备注)
        values ('$id','$name','$major','$gender','$birthday','$sum_credit','$note')";
      
        // 执行插入操作并判断结果
        if ($conn->query($sql) == true) {
            // 插入成功，显示提示并跳转回首页
            echo ("<script>alert('yes! add successfully!')</script>");
            echo ("<script>window.location.href='index.html'</script>");
        } else {
            // 插入失败，显示提示并跳转回首页
            echo ("<script>alert('oops add failed!')</script>");
            echo ("<script>window.location.href='index.html'</script>");
        }
        $conn->close(); // 关闭数据库连接
    }
    ?>
</body>

</html>

```

### 删除功能实现

delete.php实现删除的功能

```php
//delete.php
<?php
// 创建与 MySQL 数据库的连接
$conn = new mysqli("localhost", "root", "root", "xscj") or die("连接失败");
// 设置数据库连接的字符集为 GBK
$conn->query("SET NAMES gbk");

// 获取 URL 中的 ID 参数，表示要删除的学生编号
$number = $_GET['ID'];

// 构造删除 SQL 语句
$sql = "delete from xs where 学号=$number";

// 执行删除操作并判断结果
if ($conn->query($sql) === true) {
    // 如果删除成功，显示成功提示并跳转到概览页面
    echo "<script>alert('delete successfully!')</script>";
    echo "<script>window.location.href='./overview.php'</script>";
} else {
    // 如果删除失败，显示失败提示并跳转到概览页面
    echo "<script>alert('delete failed!')</script>";
    echo "<script>window.location.href='./overview.php'</script>";
}

// 关闭数据库连接
$conn->close();

```

### 主页展示功能

参照index.html

```html
<!doctype html>
<html>

<head>
    <meta charset="GBK">
    <title>主界面功能</title>
    <style>
        /* 设置背景图片和样式 */
        body {
            background-image: url(./君名.png);
            background-repeat: no-repeat;
            background-size: cover;
            background-attachment: fixed;
        }

        /* 居中显示链接 */
        .center-links {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
        }

        /* 链接按钮样式 */
        .center-links a {
            display: inline-block;
            border: 2px solid black;
            border-radius: 20px;
            padding: 5px;
            margin: 5px;
            background-image: linear-gradient(to right, #0849ebf5, #e6134f);
            text-decoration: none;
            font-size: 32px;
            color: black;
        }

        /* 作者信息样式 */
        .author {
            text-align: center;
            color: red;
            position: fixed;
            bottom: 0px;
            width: 100%;
            text-align: center;
        }
    </style>
</head>

<body>
    <!-- 页面标题 -->
    <h1 style="text-align: center;color: white;">学生管理系统</h1>
  
    <!-- 链接按钮容器 -->
    <div class="center-links">
        <div class="row">
            <!-- 查看所有学生的链接 -->
            <a href="./overview.php" target="_self">查看所有学生</a>
            <br>
            <!-- 添加新学生的链接 -->
            <a href="./add.html" target="_self">添加新的学生</a>
            <br>
            <!-- 查询指定学生的链接 -->
            <a href="./search.html" target="_self">查询指定的学生</a>
            <br>
            <!-- 返回登录界面的链接 -->
            <a href="./login.html">返回登陆界面</a>
        </div>
    </div>
</body>

</html>

```

### 修改功能实现

Modify.php,modify2.php来用实现修改学生的信息

```php
//Modify.php
<?php
// 连接到 MySQL 数据库
$conn = new mysqli("localhost", "root", "root", "xscj") or die("连接失败");
// 设置数据库连接的字符集为 GBK
$conn->query("SET NAMES gbk");
?>

<html>

<head>
    <title>修改学生的相关信息</title>
    <meta http-equiv="Content-Type" content="text/html; charset=GBK">
    <style>
        /* 设置背景图片和样式 */
        body {
            background-image: url(./君名.png);
            background-repeat: no-repeat;
            background-size: cover;
            background-attachment: fixed;
        }

        /* 表单样式 */
        form {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: white;
            line-height: 25px;
        }

        form label {
            text-align: center;
        }

        /* 提交和重置按钮样式 */
        form input[type="submit"] {
            background-color: red;
            color: white;
            margin-top: 10px;
            margin-right: 5px;
        }

        form input[type="reset"] {
            background-color: blue;
            color: white;
            margin-top: 10px;
            margin-left: 5px;
        }

        form input[type="submit"],
        form input[type="reset"] {
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        /* 单选按钮容器样式 */
        .radio-container {
            display: flex;
        }

        .radio-container label {
            margin-right: 10px;
        }

        /* 标签样式 */
        label {
            font-size: 20px;
            height: 30px;
        }

        /* 按钮容器样式 */
        .button-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
        }

        .button-container a {
            display: inline-block;
            border: 2px solid black;
            border-radius: 10px;
            padding: 5px 10px;
            margin: 5px;
            background-image: linear-gradient(to right, #0849ebf5, #e6134f);
            text-decoration: none;
            font-size: 18px;
            text-align: center;
            color: black;
        }
    </style>
</head>

<body>
    <?php
    // 获取URL中的ID参数
    $id = $_GET['ID'];
  
    // 生成修改学生信息的表单，包含隐藏的ID字段
    echo "<form action='./modify2.php' method='post'>
        <input type='hidden' name='ID' value='" . $id . "'>
        <label for='name'> 姓名<input type='text' name='s_name' id='name'></label>
        <br>
        <label for='major'>专业名<input type='text' name='major_in' id='major'></label>
        <br>
        <div class='radio-container'>
        <label><input type='radio' value='1' name='gender' required>男</label>
        <label><input type='radio' value='0' name='gender' required>女</label>
        </div>
        <br>
        <label for='date'>出生日期<input type='date' id='date' name='date'></label>
        <br>
        <label for='credit'>总学分<input type='text' id='credit' name='credits'></label>
        <br>
        <label for='note'>备注<input type='text' id='note' name='notes'></label>
        <br>
        <div class='button-container'>
             <input type='submit' value='提交'>
             <input type='reset' value='重置'>
        </div>
        </form>";
    ?>
    <!-- 返回按钮，链接到概览页面 -->
    <div class="button-container">
        <a href="./overview.php">返回</a>
    </div>
</body>

</html>

```

```php
//modify2.php
<?php
$conn = new mysqli("localhost", "root", "root", "xscj") or die("连接失败");
$conn->query("SET NAMES gbk");
?>
<!DOCTYPE html>
<html lang="zh">

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=GBK">
    <title>学生信息修改</title>
</head>

<body>
    <?php
    $id = $_POST['ID'];
    $name = $_POST['s_name'];
    if (!empty($name)) {
        $sql = "update xs set 姓名='$name' where 学号='$id'";
        $conn->query($sql);
    }
    $major = $_POST['major_in'];
    if (!empty($major)) {
        $sql = "update xs set 专业名='$major' where 学号='$id'";
        $conn->query($sql);
    }
    $gender = $_POST['gender'];
    if (!empty($gender)) {
        $sql = "update xs set 性别='$gender' where 学号='$id'";
        $conn->query($sql);
    }
    $birthday = $_POST['date'];
    if (!empty($birthday)) {
        $sql = "update xs set 出生日期='$birthday' where 学号='$id'";
        $conn->query($sql);
    }
    $sum_credit = $_POST['credits'];
    if (!empty($sum_credit)) {
        $sql = "update xs set 总学分='$sum_credit' where 学号='$id'";
        $conn->query($sql);
    }
    $note = $_POST['notes'];
    if (!empty($note)) {
        $sql = "update xs set 备注='$note' where 学号='$id'";
        $conn->query($sql);
    }
    echo ("<script>alert('修改成功！')</script>");
    echo ("<script>window.location.href='./overview.php'</script>");
    $conn->close();
    ?>
</body>

</html>

```

### 查找功能实现

Search.html,search.php实现查找指定学生的功能在search.php中模糊搜索的底层逻辑是通过学生的姓名用like关键字进行查询，

而精确搜索是通过学生的学号进行查询，一般只会有一条数据，因为我限制了学号是唯一的。代码这里不做展示，因为太长了。

```html
Search.html
<!doctype html>
<html>

<head>
    <meta charset="GBK">
    <title>查找指定的学生</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            background-image: url(./君名.png);
            background-repeat: no-repeat;
            background-size: cover;
            background-attachment: fixed;
        }

        h1 {
            text-align: center;
            color: white;
        }

        form {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        input[type="text"] {
            width: 200px;
            height: 30px;
            margin-bottom: 10px;
        }

        input[type="submit"] {
            width: 120px;
            height: 30px;
            margin-bottom: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            color: white;
        }

        input[value="精确查询"] {
            background-color: red;
        }

        input[value="模糊搜索"] {
            background-color: blue;
        }

        .button-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
        }

        .button-container a {
            display: inline-block;
            border: 2px solid black;
            border-radius: 10px;
            padding: 5px 10px;
            margin: 5px;
            background-image: linear-gradient(to right, #0849ebf5, #e6134f);
            text-decoration: none;
            font-size: 18px;
            text-align: center;
            color: black;
        }
    </style>
</head>

<body>

    <h1>请输入您想查询的学生的学号或者是姓名</h1>
    <form action="./search.php" method="post">
        <input type="text" name="id">
        <br>
        <input type="submit" value="精确查询" name="exact">
        <input type="submit" value="模糊搜索" name="fuzzy">
    </form>
    <br>
    <h4 style="text-align: center;color: red;">!!!注意:模糊搜索只能通过输入学生的姓名进行搜索，精确搜索只能通过输入学生的学号进行搜索</h4>
    <div class="button-container">
        <a href="./index.html">返回</a>
    </div>

</body>

</html>

```

```php
//search.php
<?php
$conn = new mysqli("localhost", "root", "root", "xscj") or die("连接失败");
$conn->query("SET NAMES gbk");
?>
<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="GBK">
    <title>查询学生</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            background-image: url(./君名.png);
            background-repeat: no-repeat;
            background-size: cover;
            background-attachment: fixed;
        }

        h1 {
            color: red;
        }

        table {
            margin-top: 20px;
            border-collapse: collapse;
            width: 80%;
        }

        th,
        td {
            padding: 8px;
            text-align: center;
        }

        th {
            background-color: blue;
            color: white;
        }

        tr:nth-child(even) {
            background-color: #f2f2f2;
        }

        a.button {
            display: inline-block;
            padding: 8px 16px;
            text-align: center;
            text-decoration: none;
            background-color: red;
            color: white;
            border-radius: 5px;
            margin-right: 5px;
        }

        a.button.blue {
            background-color: blue;
        }

        .return {
            display: inline-block;
            border: 2px solid black;
            border-radius: 20px;
            padding: 5px;
            margin: 5px;
            background-image: linear-gradient(to right, #0849ebf5, #e6134f);
            text-decoration: none;
            font-size: 32px;
            text-align: center;
            color: black;
        }
    </style>
</head>

<body>
    <table border="1">
        <?php
        if (isset($_POST['exact']) && !empty($_POST['id'])) {
            $id = $_POST['id'];
            $sql = "SELECT * FROM xs WHERE 学号='$id'";
            $result = $conn->query($sql);
            if ($result->num_rows > 0) {
                echo "<h1>一共查询到 " . $result->num_rows . " 条数据</h1>";
                echo "<tr>
                    <th>学号</th>
                    <th>姓名</th>
                    <th>专业名</th>
                    <th>性别</th>
                    <th>出生日期</th>
                    <th>总学分</th>
                    <th>备注</th>
                    <th>功能</th>
                </tr>";
                while ($row = $result->fetch_assoc()) {
                    echo "<tr>";
                    echo "<td>{$row['学号']}</td>";
                    echo "<td>{$row['姓名']}</td>";
                    echo "<td>{$row['专业名']}</td>";
                    echo "<td>{$row['性别']}</td>";
                    echo "<td>{$row['出生日期']}</td>";
                    echo "<td>{$row['总学分']}</td>";
                    echo "<td>{$row['备注']}</td>";
                    echo "<td>
                        <a class='button' href='delete.php?ID={$row['学号']}'>删除</a>
                        <a class='button blue' href='modify.php?ID={$row['学号']}'>修改</a>
                    </td>";
                    echo "</tr>";
                }
            } else {
                echo "<tr><td colspan='8'>查无此人</td></tr>";
            }
        } elseif (isset($_POST['fuzzy']) && !empty($_POST['id'])) {
            $id = $_POST['id'];
            $sql = "SELECT * FROM xs WHERE 姓名 LIKE '%$id%'";
            $result = $conn->query($sql);
            if ($result->num_rows > 0) {
                echo "<h1>一共查询到 " . $result->num_rows . " 条数据</h1>";
                echo "<tr>
                    <th>学号</th>
                    <th>姓名</th>
                    <th>专业名</th>
                    <th>性别</th>
                    <th>出生日期</th>
                    <th>总学分</th>
                    <th>备注</th>
                    <th>功能</th>
                </tr>";
                while ($row = $result->fetch_assoc()) {
                    echo "<tr>";
                    echo "<td>{$row['学号']}</td>";
                    echo "<td>{$row['姓名']}</td>";
                    echo "<td>{$row['专业名']}</td>";
                    echo "<td>{$row['性别']}</td>";
                    echo "<td>{$row['出生日期']}</td>";
                    echo "<td>{$row['总学分']}</td>";
                    echo "<td>{$row['备注']}</td>";
                    echo "<td>
                        <a class='button' href='delete.php?ID={$row['学号']}'>删除</a>
                        <a class='button blue' href='modify.php?ID={$row['学号']}'>修改</a>
                    </td>";
                    echo "</tr>";
                }
            } else {
                echo "<tr><td colspan='8'>查无此人</td></tr>";
            }
        } else {
            echo "<tr><td colspan='8'>数据为空, 因为您并未输入有效的信息！</td></tr>";
        }
        ?>
    </table>
    <a href="./index.html" class="return">返回主界面</a>
</body>

</html>

```

### 展示所有学生信息

Overview.php用来展示所有学生的信息

```php
//Overview.php
<?php
$conn = new mysqli("localhost", "root", "root", "xscj") or die("连接失败");
// $conn->query("SET NAMES gbk");
?>

<html>

<head>
    <title>学生管理系统</title>
    <meta charset="GBK">
    <style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            background-image: url(./君名.png);
            background-repeat: no-repeat;
            background-size: cover;
            background-attachment: fixed;
        }

        h1 {
            color: blue;
        }

        table {
            margin-top: 20px;
            border-collapse: collapse;
            width: 80%;
        }

        th,
        td {
            padding: 8px;
            text-align: center;
        }

        th {
            background-color: blue;
            color: white;
        }

        tr:nth-child(even) {
            background-color: #f2f2f2;
        }

        a.button {
            display: inline-block;
            padding: 8px 16px;
            text-align: center;
            text-decoration: none;
            background-color: red;
            color: white;
            border-radius: 5px;
            margin-right: 5px;
        }

        a.button.blue {
            background-color: blue;
        }

        .return {
            display: inline-block;
            border: 2px solid black;
            border-radius: 20px;
            padding: 5px;
            margin: 5px;
            background-image: linear-gradient(to right, #0849ebf5, #e6134f);
            text-decoration: none;
            font-size: 32px;
            text-align: center;
            color: black;
        }
    </style>
</head>

<body>
    <h1>学生信息展示</h1>
    <table border="2">
        <tr>
            <th>学号</th>
            <th>姓名</th>
            <th>专业名</th>
            <th>性别</th>
            <th>出生日期</th>
            <th>总学分</th>
            <th>备注</th>
            <th>功能</th>
        </tr>
        <?php
        $sql = "select * from xs";
        $result = $conn->query($sql);
        if ($result->num_rows > 0) {
            while ($row = $result->fetch_assoc()) {
                echo "<tr>";
                echo "<td>{$row['学号']}</td>";
                echo "<td>{$row['姓名']}</td>";
                echo "<td>{$row['专业名']}</td>";
                echo "<td>{$row['性别']}</td>";
                echo "<td>{$row['出生日期']}</td>";
                echo "<td>{$row['总学分']}</td>";
                echo "<td>{$row['备注']}</td>";
                echo "<td><a href='delete.php?ID={$row['学号']}' class='button'>删除</a>
                <a href='modify.php?ID={$row['学号']}' class='button blue'>修改</a></td>";
                echo "</tr>";
            }
        } else {
            echo "<tr><td colspan='8'>没有输出结果</td></tr>";
        }
        $conn->close();
        ?>
    </table>
    <br>
    <br>
    <a href="./index.html" class="return">返回主界面</a>
</body>

</html>
```

## 结语

有任何问题，可以在评论区给我留言🤔
