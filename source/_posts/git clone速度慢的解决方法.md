---
title: 关于git clone速度极慢的解决方法
date: 2024-07-16 19:19:40
tags: 杂文
---
## 前言

我在写这篇文章前，也搜索过很多相关git clone速度很慢的解决方法，但是很多很麻烦，或者是非常的不稳定，我在自己无意间尝试中发现了一个可以很稳定给git clone提速的方法，那就是通过使用代理的方法来进行提速，因此如果你没有一个可靠且稳定的梯子，接下来的就不用看了

## 尝试过的方法(未成功)

既然有成功，那么在探索过程中也必定会有失败的方法，下面也介绍一下我试过的没啥用的方法，给各位避雷，不用花时间去刻意尝试了😊😊

### 更改github的hosts/使用steam++（用处不大）

这两个方法本质上都是一样的，就是改hosts，网上说(**不是我说的哈，与本人没有任何的关系**)是github的dns会被不定时污染，所以访问起来特别的慢

![img](https://raw.githubusercontent.com/kashima19960/img/master/git%20clone%E9%80%9F%E5%BA%A6%E6%85%A2%E7%9A%84%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95/afbb21aff4e2475393c71518b7db7dc6.png)

典中典🤣，然后通过给定github的hosts，让dns能够解析到ping值低的服务器上。但是这种方法对git clone 的下载速度没啥用（亲测），不过有时候访问github网页还是行的，具体的可以参照这个https://github.com/521xueweihan/GitHub520.git

### 将github的项目导入到gitee中(有用，但是麻烦的要死)

这个就不必讲步骤了，确实能显著提高git clone的速度，毕竟gitee的服务器在国内，但是很麻烦

## 让git使用proxy（魔法，亲测有效果而且很简单）

我试过用🐱挂梯子，然后再github上直接点击Code里面的Download ZIP

![img](https://raw.githubusercontent.com/kashima19960/img/master/git%20clone%E9%80%9F%E5%BA%A6%E6%85%A2%E7%9A%84%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95/43c4d3ecbeb74237bdf127dc4d68d282.png)

这样的下载速度能显著提高，但是这样是无法把git仓库也克隆下来的，而且挂梯子只能作用于浏览器的浏览，对于命令行的git clone是没有作用的，于是！我查阅git的官方文档发现git本身也是可以使用代理的，在命令行中可以这样

```bash
git config --global http.proxy 127.0.0.1:port
git config --global https.proxy 127.0.0.1:port
```

很多教程中都不会解释这个port端口号要如何设置，或者是随便填一个莫名其妙的端口号，造成类似以下的报错

```bash
fatal: unable to access 'https://github.com/xxxxxx': Failed to connect to 127.0.0.1 port 1082 after 2075 ms: Couldn't connect to server
```

实际上这个端口号是不能乱填的。应该被设置你的代理软件所使用的端口号，比如我自己使用的是🐱，他的默认端口为

![img](https://raw.githubusercontent.com/kashima19960/img/master/git%20clone%E9%80%9F%E5%BA%A6%E6%85%A2%E7%9A%84%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95/3fe9be36296246c59bb87eea8e34e6da.png)

或者我不喜欢用命令行敲代码的方式进行代理设置，图形化界面更友好一点，该怎么办呢？

其实也可以这样，用任意的文本编辑器打开"C:\Users\你自己的创建的用户\.gitconfig"，然后在这个文件输入就行了

![img](https://raw.githubusercontent.com/kashima19960/img/master/git%20clone%E9%80%9F%E5%BA%A6%E6%85%A2%E7%9A%84%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95/6833f24c911c4e9586ab37b2329ffa41.png)

## 效果

### 使用代理前

![img](https://raw.githubusercontent.com/kashima19960/img/master/git%20clone%E9%80%9F%E5%BA%A6%E6%85%A2%E7%9A%84%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95/a0fd1740a6d34822b2bf8602930b4fa6.png)

12.00kib/s什么概念？我tmd某云盘下载速度都比这快👿

### 使用代理后

![img](https://raw.githubusercontent.com/kashima19960/img/master/git%20clone%E9%80%9F%E5%BA%A6%E6%85%A2%E7%9A%84%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95/a2f9380496e5480892871a12cde87e5a.png)速度虽然说也不是很快，但也改善了很多了😊
