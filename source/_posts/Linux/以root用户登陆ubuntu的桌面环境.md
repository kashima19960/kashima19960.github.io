---
title: 以root用户登陆ubuntu的桌面环境
date: 2024-09-16 16:58:00
tags: Linux
---

## 前言

在学习Linux的时候，经常都需要使用sudo权限来对配置文件进行修改，常用的方法就是用vim编辑器在命令行界面进行修改，比如`sudo vim /etc/profile`，但我觉得每次都用命令行挺麻烦的，于是！🤓我就想办法直接用root用户的方法登陆桌面，然后用桌面的GUI编辑器直接编辑文本。下面的操作步骤是基于Ubuntu的，不过只要是使用**Gnome桌面**的发行版应该都是适用的

>   GNOME桌面环境是一个免费的开源桌面环境，最初是为Linux和其他类Unix操作系统开发的。GNOME的全称是GNU网络对象模型环境（GNU Network Object Model Environment），它旨在为用户提供一个友好且易于使用的图形界面。许多主要的Linux发行版，如Debian、Fedora、Ubuntu等，都将GNOME作为默认桌面环境

## 重要提示！！

默认情况下，你没办法直接通过root用户登陆桌面，因为这相当的危险(可以不限制对所有文件进行操作)，所以这个做法被官方限制了。在以root用户登陆桌面后，请谨慎进行操作！！

## 第 1 步：启用 root 账户

root用户一般是没有密码的，默认情况下不启用。使用`sudo passwd root`来给root用户得到一个密码,需要注意的是，用sudo改密码是可以无视密码策略的，也就是说像“1”,”123”,”111”这样的简单密码也是可以修改成功的，因此最好要记住你自己设置的root密码。

![image-20240916171827876](https://raw.githubusercontent.com/kashima19960/img/master/%E4%BB%A5root%E7%94%A8%E6%88%B7%E7%99%BB%E9%99%86ubuntu%E7%9A%84%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83%20/image-20240916171827876.png)

## 第2步：更改 GDM 配置

gdm,全称gnome display managers,如字面意思，他的作用是提供gnome桌面的图形登录并处理用户身份验证，现在都是用gdm3了，我们需要修改他的配置文件,使用

```bash
sudo vim /etc/gdm3/custom.conf
```

如果你不会用vim编辑器，那么用nano也行，比较简单。

```bash
sudo nano /etc/gdm3/custom.conf
```

然后在[daemon]下面添加,意思就是允许root用户登陆

```bash
AllowRoot=true
```



![image-20240916174416908](https://raw.githubusercontent.com/kashima19960/img/master/%E4%BB%A5root%E7%94%A8%E6%88%B7%E7%99%BB%E9%99%86ubuntu%E7%9A%84%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83%20/image-20240916174416908.png)

最后保存退出

## 第 3 步：配置 PAM 认证

打开 PAM 认证守护进程文件

```bash
sudo vim /etc/pam.d/gdm-password
```

在这个文件中找到

```bash
auth   required        pam_succeed_if.so user != root quiet_success
```

然后在这一行前面加上一个`#`，表示注释掉这一行，因为这一行拒绝了在GUI中的root访问权限

```bash
# auth   required        pam_succeed_if.so user != root quiet_success
```

最后保存退出

## 第4步:登陆root用户

在做出上述修改后，要重启一下，不然修改不会生效

之后在用户登陆界面，下面会有个很小的一行字`not list？`，要是你设置了系统语言为中文的话就是`未列出？`,点击进行用root用户登陆就行了

![轻松 DIY：Ubuntu 登录与锁屏壁纸定制全攻略 - 系统极客](https://raw.githubusercontent.com/kashima19960/img/master/%E4%BB%A5root%E7%94%A8%E6%88%B7%E7%99%BB%E9%99%86ubuntu%E7%9A%84%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83%20/change-ubuntu-22-04-login-screen-background-8.jpg)

登陆成功后，会提示

![image-20240916175400174](https://raw.githubusercontent.com/kashima19960/img/master/%E4%BB%A5root%E7%94%A8%E6%88%B7%E7%99%BB%E9%99%86ubuntu%E7%9A%84%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83%20/image-20240916175400174.png)

大致意思就是，你现在在用特权账户登陆，这个操作应该被避免。出现这个对话框，说明就成功用root用户登陆桌面环境了！