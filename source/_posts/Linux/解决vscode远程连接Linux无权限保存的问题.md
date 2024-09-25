---
title: 解决vscode远程连接Linux无权限保存的问题
date: 2024-09-25 10:05:00
tags: Linux
---

## 存在的问题

用vscode远程登陆普通用户修改/etc/profile，保存文件时，出现了以下的问题。大体意思就是没有权限进行更改。

![image-20240925100746008](https://raw.githubusercontent.com/kashima19960/img/master/%E8%A7%A3%E5%86%B3vscode%E8%BF%9C%E7%A8%8B%E8%BF%9E%E6%8E%A5Linux%E6%97%A0%E6%9D%83%E9%99%90%E4%BF%9D%E5%AD%98%E7%9A%84%E9%97%AE%E9%A2%98%20/image-20240925100746008.png)

## 解决方法

通常情况下，普通用户只能对自己home目录里面的文件进行更改，想要修改home目录以外的文件通常来说都是需要root权限的，在命令行界面可以利用vim编辑器配合`sudo`来达到这个目的，但是vscode的GUI编辑器里面是没有提供类似的功能的，如果想要通过vscode自带的编辑器修改没有权限的文件，可以通过这个插件

![image-20240925102457046](https://raw.githubusercontent.com/kashima19960/img/master/%E8%A7%A3%E5%86%B3vscode%E8%BF%9C%E7%A8%8B%E8%BF%9E%E6%8E%A5Linux%E6%97%A0%E6%9D%83%E9%99%90%E4%BF%9D%E5%AD%98%E7%9A%84%E9%97%AE%E9%A2%98%20/image-20240925102457046.png)

按下`ctrl+shift+p`,输入`save as root`

![image-20240925102621847](https://raw.githubusercontent.com/kashima19960/img/master/%E8%A7%A3%E5%86%B3vscode%E8%BF%9C%E7%A8%8B%E8%BF%9E%E6%8E%A5Linux%E6%97%A0%E6%9D%83%E9%99%90%E4%BF%9D%E5%AD%98%E7%9A%84%E9%97%AE%E9%A2%98%20/image-20240925102621847.png)

可以看到文件成功保存了

![image-20240925102719335](https://raw.githubusercontent.com/kashima19960/img/master/%E8%A7%A3%E5%86%B3vscode%E8%BF%9C%E7%A8%8B%E8%BF%9E%E6%8E%A5Linux%E6%97%A0%E6%9D%83%E9%99%90%E4%BF%9D%E5%AD%98%E7%9A%84%E9%97%AE%E9%A2%98%20/image-20240925102719335.png)