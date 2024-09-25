---
title: Windows的cmd使用Linux类命令
date: 2024-08-13 23:20:00
tags: Linux
---
## 前言

我在使用Vscode编写C/C++代码的时候，经常会用到**Shell**(你可以理解为命令行)，但是我不得不说Windows下Dos命令极其难用且拉跨😩，于是！！🤓🤓我就在想能不能在Windows的命令提示符或者PowerShell下直接使用Linux的命令，然后我就在中文互联网上疯狂的搜索(💩里淘金)

## 存在的问题

在中文互联网上搜索问题，通常都会得到以下的结果

![image-20240812235813091](https://cdn.jsdelivr.net/gh/kashima19960/img@master/Win%E7%B3%BB%E7%BB%9F%E4%BD%BF%E7%94%A8Linux%E5%91%BD%E4%BB%A4%20/image-20240812235813091.png)

他们给出的结果，无非就是

1. 使用WSL或者是在虚拟机里面使用Linux

   个人评价：可真是个小天才呢😅，这样我为啥不直接用Linux呢？还折腾那么多干嘛
2. 使用Git Bash或者Cygwin

   个人评价:太丑

更让我觉得好笑的是，这些文章都是搬的外网的一个博主的文章[4 Ways to Run Linux Commands in Windows (itsfoss.com)](https://itsfoss.com/run-linux-commands-in-windows/)，搜索引擎一排下去都是差不多的内容，这还是在我屏蔽了csdn相关结果的情况下(关于如何屏蔽csdn的搜索结果可以看我的另一篇文章)，可见要想在中文互联网找到解决自己需求的方法有多困难。

![image-20240813003550182](https://cdn.jsdelivr.net/gh/kashima19960/img@master/Win%E7%B3%BB%E7%BB%9F%E4%BD%BF%E7%94%A8Linux%E5%91%BD%E4%BB%A4%20/image-20240813003550182.png)

## 解决方法

综上所述，经过我的一般探索，找到了一个可以在Windows运行Linux类命令的工具——**uutils-coreutils**,通过官网的简介可以得知

> uutils is an attempt at writing universal (as in cross-platform) CLI utilities in [Rust](https://www.rust-lang.org/). It is available for Linux, Windows, Mac and other platforms.

翻译成人话就是，这玩意是一个用 [Rust](https://www.rust-lang.org/) 编写通用（**跨平台**）CLI 实用工具的项目。它可用于 Linux、Windows、Mac 和其他平台。啊哈👍跨平台而且还是CLI实用工具的项目，这正是我想要的！

![image-20240813003942634](https://cdn.jsdelivr.net/gh/kashima19960/img@master/Win%E7%B3%BB%E7%BB%9F%E4%BD%BF%E7%94%A8Linux%E5%91%BD%E4%BB%A4%20/image-20240813003942634.png)

### 效果图

讲再多，不如直接看看效果，这个工具包含了很多Linux下的常用且基本的命令

最常用的ls命令，其中一些常用的参数也是可以使用的，比如-a,-l

![image-20240813004739055](https://cdn.jsdelivr.net/gh/kashima19960/img@master/Win%E7%B3%BB%E7%BB%9F%E4%BD%BF%E7%94%A8Linux%E5%91%BD%E4%BB%A4%20/image-20240813004739055.png)

删除文件的rm命令，这个是通过VSCode的集成终端调用的，这样在vscode里面就能直接使用Linux命令了

![image-20240813004927238](https://cdn.jsdelivr.net/gh/kashima19960/img@master/Win%E7%B3%BB%E7%BB%9F%E4%BD%BF%E7%94%A8Linux%E5%91%BD%E4%BB%A4%20/image-20240813004927238.png)

### 安装方法

安装这个软件有两种方法

1. 通过包管理下载

   Windows下常见的包管理器有Scoop(博主用的是这个)或者Winget,其他的系统你可以看看官方文档[Installation - uutils Documentation](https://uutils.github.io/coreutils/docs/installation.html)，都有对应的命令，复制粘贴到对应系统的命令行就行了

   > 如果你不知道啥是包管理器的话，简单来说就是类似于手机的应用商店一样，能帮你一键安装软件，包括安装依赖以及添加环境变量等等。
   >
   > Scoop的安装可以参照[官方文档](https://github.com/ScoopInstaller/Scoop#installation)，这里不做赘述
   >
2. 下载Github release打包好的程序

[Release 0.0.27 · uutils/coreutils (github.com)](https://github.com/uutils/coreutils/releases/tag/0.0.27)

在Assets这里选择适合你系统的进行下载即可

![image-20240813010032620](https://cdn.jsdelivr.net/gh/kashima19960/img@master/Win%E7%B3%BB%E7%BB%9F%E4%BD%BF%E7%94%A8Linux%E5%91%BD%E4%BB%A4%20/image-20240813010032620.png)

Windows系统的话，安装完后可能得手动添加软件根目录的路径到系统的环境变量中，不然的话在命令行中可能会找不到相应的命令
