---
title: 在VMware配置Ubuntu20.04静态ip的方法
date: 2024-11-30 11:35:00
tags: Linux
---

## 前言

本文适用于在Windows下配置VMware虚拟机NAT模式下的静态ip，如果你与我使用的软件版本不一样的话，那么配置操作仅供参考

### 软件版本

-   ubuntu20.04
-   VMware17

## Just do it!

打开window的网络适配器更改的选项，不同window版本的入口会有所差异，所以请自行寻找。VMware会创建多个虚拟网卡VMnet，命名如下图所示，每台电脑的虚拟网络命名都可能不同，这里我们选择`VMnet8`,这里记住这个网络的名字，后面要考😋

![image-20241130114230277](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/image-20241130114230277.png)

点击属性

![image-20241130114929350](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/image-20241130114929350.png)

找到ipv4这一栏，点进去，修改ip

![image-20241130115031196](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/image-20241130115031196.png)

因为下面的内容都会涉及到计算机网络的知识，因此如果你没学过计算机网络的话，别想太多，做就完事了。

### 说明

1.   IP地址你只能设置为三大私有地址段(不做阐述)，这里推荐使用`192.168.1xxx.2xxx`这个私有地址
2.   `1xxx`可以随便填从`0~255`任意值，我下面填了`235`
3.   `2xxx`一般要用来标识子网地址，所以最好填`0`或者`1`
4.   C类地址的网络号是24位，因此子网掩码固定填写`255.255.255.0`
5.   默认网关要跟ip地址在同一个子网，别跟ip地址重复就行
6.   DNS不要填，让他自动配置

修改完后点确定就行

![image-20241130115123230](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/image-20241130115123230.png)

之后打开VMware的虚拟网络编辑器，找到`Vmnet8`(前面的伏笔哦),把DHCP取消掉，这个功能会自动帮你分配ip,但这不是你想要的！😈

![image-20241130120351824](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/image-20241130120351824.png)

然后打开NAT设置,这里的网关要跟前面在Windows设置的一样

![image-20241130120613803](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/image-20241130120613803.png)

虚拟机，启动！在设置里面打开网络配置，这里唯一要注意的是**网关要跟DNS的地址设置成一样的**，要不然ping网站的时候会出现域名解析错误！！

![image-20241130120801311](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/image-20241130120801311.png)

配置完后要重启电脑，之后我们试试ping一下百度，看看是否能成功

![image-20241130121018849](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/image-20241130121018849.png)

然后在看看ip地址是否配置成功,我的虚拟机网络是ens33，可以ip地址变成了`192.168.235.15`

```bash
$ ifconfig
ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.235.15  netmask 255.255.255.0  broadcast 192.168.235.255
        inet6 fe80::39b5:326e:53f9:de8a  prefixlen 64  scopeid 0x20<link>
        inet6 fd15:4ba5:5a2b:1008:f6fa:23d4:56df:a104  prefixlen 64  scopeid 0x0<global>
        inet6 fd15:4ba5:5a2b:1008:c61a:74ad:3acf:44cc  prefixlen 64  scopeid 0x0<global>
        ether 00:0c:29:20:3a:79  txqueuelen 1000  (以太网)
        RX packets 135957  bytes 20951062 (20.9 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 139753  bytes 26594213 (26.5 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (本地环回)
        RX packets 331  bytes 32082 (32.0 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 331  bytes 32082 (32.0 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

```

