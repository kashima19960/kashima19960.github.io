---
title: Iptables，ufw，firewalld的关系与区别
date: 2024-09-26 21:44:00
tags: Linux
---

## iptables
定义：iptables 是 Linux 内核中用于设置和维护 IP 数据包过滤规则的工具。它允许用户创建、管理和检查一系列的规则，这些规则定义了如何处理进入或离开系统的数据包。iptables 是一个底层工具，提供了强大的灵活性和控制能力，但同时也需要用户具备一定的网络知识来有效配置。

**用人话总结：用来过滤网络流量的工具，很底层的意思就是非常难用且复杂。**

## ufw

定义：ufw 是一个为简化 iptables 配置而设计的前端工具，特别适合于主机防火墙的设置。它通过提供简单的命令行界面，使得用户能够轻松地允许或阻止特定端口的流量。虽然 ufw 实际上依赖于 iptables 来实现其功能，但它隐藏了许多复杂性，使得防火墙配置变得更为直观和易于管理。

**用人话总结：iptables不是很底层吗？ufw做的就是将iptables很难用且复杂的底层操作封装成几个很简单的命令，帮你省去一大堆参数和选项。**

## firewalld

firewalld 是 Red Hat 开发的一种动态防火墙管理工具，它同样可以作为 iptables 或 nftables 的前端。与 ufw 相比，firewalld 提供了更为复杂和灵活的功能，包括支持不同网络接口的不同规则集（称为区域）以及运行时和永久配置的管理

**用人话总结：和ufw一样封装了iptables，区别就是操作比ufw复杂一点**。

## 该选择那个？

**不同的防火墙工具，一起使用是会起冲突的，所以不能混合使用**。拿windows类似的软件类比一下就知道了，360安全卫士和金山毒霸能相容吗？🫠🫠

按使用难度来说:iptables>firewalld>ufw。ufw是最简单的了，命令也好记，参数和选项也没几个。

按功能复杂度来说:firewalld>ufw>iptables。firewalld适合需要复杂网络环境管理的大型服务器或企业级应用，大型开发就用firewalld。

另外提一嘴，

-   **UFW**: 默认用于 **Ubuntu** 及其衍生版（如 Kubuntu、Xubuntu 等），也可在一些 Debian 系统中使用。
-   **firewalld**: 默认用于 **Red Hat**、**CentOS** 和 **Fedora** 等发行版。
