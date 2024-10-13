---
title: wsl2启用代理(梯子)的方法
date: 2024-10-13 15:18:12
tags: Linux
---

## 前言

开头先讲讲wsl2启用代理的必要性，一般来说，会用wsl的都是开发者，那么就避免不了从网络上下载软件和应用，但是由于众所周知的原因，你使用apt，wget等工具下载国外网站的东西时，下载速度就会非常的缓慢，因此让wsl2使用代理是提高下载速度的有效手段。通常情况下，wsl2的网络会采用NAT模式，如果你不知道啥是NAT,这里我简单介绍一下

### NAT模式

**Network Address Translation**(NAT)，翻译过来就是网络地址转换，别看网上的定义那么复杂，其实这个东西很简单，就是将你本地的ip地址与一台有公网ip地址的服务器做一个简单的映射

| 公网ip    | 本地ip      |
| --------- | ----------- |
| 113.x.x.x | 192.168.x.x |

现实中，一般都会有多个本地ip映射到同一个公网ip上，这样就能多台电脑同时使用一个公网ip，节约公网ip的数量，而且通常来说，NAT都是会进行多次映射的，所以就会有二次nat，三次nat这种东西。因此计算机领域很大的一个特点就是套娃捏😂😂。

ok，回到正题，如何你在使用代理的情况下启动wsl，通常会得到以下的提示

```bash
wsl: 检测到 localhost 代理配置，但未镜像到 WSL。NAT 模式下的 WSL 不支持 localhost 代理。
```

## 解决方法

不支持NAT，那么就改成其他模式就好了，具体的步骤如下

1.   在你windows的用户文件夹下找到一个`.wslconfig`的文件，如果没有那你就自己创建一个，用户文件夹的路径通常是`C:\Users\<这里是你自己的用户名>`
2.   在这个文件夹中输入以下的内容,networkingMode就是网络模式，默认是NAT，这里我们改成`mirrored`,镜像模式就是与windows本机的网络配置一样

```bash
[wsl2]	
networkingMode=mirrored
autoProxy=true
```

3.   重启wsl

```bash
wsl --shutdown
wsl
```

上面的方法是我查阅官方文档后总结出来的,[WSL 中的高级设置配置 | Microsoft Learn](https://learn.microsoft.com/zh-cn/windows/wsl/wsl-config),想要配置其他的选项可以参考。如果你是一个小白，我不推荐你看微软的官方文档，因为很难看懂，如果你已经是老手，那么我建议你看英文版的，因为微软官翻的中文，我只能说忍俊不禁🤓

## 结果

改成镜像模式后，wsl的ip地址会和windows本机的相同

```bash
$ ifconfig 
eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.77.27.220  netmask 255.255.255.0  broadcast 10.77.27.255
        inet6 fe80::5591:8540:66e9:2273  prefixlen 64  scopeid 0x20<link>
        ether b0:25:aa:58:2d:bc  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 12  bytes 976 (976.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

可以看到ip地址都是相同的，说明修改就成功了

```bash
以太网适配器 以太网:

   连接特定的 DNS 后缀 . . . . . . . : 
   本地链接 IPv6 地址. . . . . . . . : fe80::5591:8540:66e9:2273%14
   IPv4 地址 . . . . . . . . . . . . : 10.77.27.220
   子网掩码  . . . . . . . . . . . . : 255.255.255.0
   默认网关. . . . . . . . . . . . . : 10.77.27.254
```

