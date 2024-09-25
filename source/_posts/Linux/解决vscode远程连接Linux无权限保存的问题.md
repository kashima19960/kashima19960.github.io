---
title: 解决vscode远程连接Linux无权限保存的问题
date: 2024-09-25 10:05:00
tags: Linux
---

## 存在的问题

用vscode远程登陆普通用户修改/etc/profile，保存文件时，出现了以下的问题。大体意思就是没有权限进行更改。

![image-20240925100746008](https://s2.loli.net/2024/09/25/hJpjTufCxQiLH4E.png)

## 解决方法

通常情况下，普通用户只能对自己home目录里面的文件进行更改，想要修改home目录以外的文件通常来说都是需要root权限的，在命令行界面可以利用vim编辑器配合`sudo`来达到这个目的，但是vscode的GUI编辑器里面是没有提供类似的功能的，如果想要通过vscode自带的编辑器修改没有权限的文件，可以通过这个插件

![image-20240925102457046](https://s2.loli.net/2024/09/25/vQSdkP3lJRD5fG1.png)

按下`ctrl+shift+p`,输入`save as root`

![image-20240925102621847](https://s2.loli.net/2024/09/25/oaZGPueqfKpXSnE.png)

可以看到文件成功保存了

![image-20240925102719335](https://s2.loli.net/2024/09/25/vbzfFto4gPAGseW.png)