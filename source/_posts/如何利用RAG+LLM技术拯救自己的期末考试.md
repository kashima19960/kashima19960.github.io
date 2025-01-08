---
title: 如何利用RAG+LLM技术拯救自己的期末考试
date: 2025-01-08 21:14:00
tags: 其他
---
## 前言

博主最近正在为了微机和计算机操作系统的期末考试而忙碌中(毕竟还在读大学😭)，操作系统的复习资料和复习重点都给的很全，所以我复习起来还是相当顺利的。但是，诶🤓！，接下来我要重点“表扬”一下微机这门课的各种神奇操作

1. 给了题库，但是没有答案，更没解析

![image-20250108213235278](https://cdn.jsdelivr.net/gh/kashima19960/img@master/RAG%E5%92%8CLLM%E6%8A%80%E6%9C%AF%E6%90%AD%E5%BB%BA%E7%9F%A5%E8%AF%86%E5%BA%93/image-20250108213235278.png)

PS:这个题库有好几万字😅
2.   抽象的书籍

![微型计算机技术及应用 的图像结果](https://cdn.jsdelivr.net/gh/kashima19960/img@master/RAG%E5%92%8CLLM%E6%8A%80%E6%9C%AF%E6%90%AD%E5%BB%BA%E7%9F%A5%E8%AF%86%E5%BA%93/%E5%BE%AE%E6%9C%BA%E4%B9%A6%E5%B0%81%E9%9D%A2.jpeg)

这本书谁看谁知道，这么抽象的书，能学明白的是这个👍，而且知识点还多，想要短时间内复习完，那是相当困难的。

所以我找到了一种利用**RAG技术+LLM**（大语言模型，比较有名的是ChatGPT）搭建出问答系统，让这个问答系统来帮我做题和复习的方法。

> 仅以此文章记录这一流程，文中用到的技术可能会过时，这个可以寻找一下平替，但是解决问题的思路是不会过时的

## 效果展示

我向来喜欢先展示出效果，因为这样读者才能快速地知道，接下来的一系列操作所耗费的精力是否值得😋

这个是问题目怎么做

![image-20250108222106777](https://cdn.jsdelivr.net/gh/kashima19960/img@master/RAG%E5%92%8CLLM%E6%8A%80%E6%9C%AF%E6%90%AD%E5%BB%BA%E7%9F%A5%E8%AF%86%E5%BA%93/image-20250108222106777.png)

如果你直接找一个LLM问某个领域很高深且具体的题目的话，会有非常高的概率出现**大模型幻觉**，所谓的**幻觉**，其实就是“说胡话”，LLM看似回答了你很多内容，但是当你仔细看看可能会发现，他就是在胡扯，完全不清楚他回答的根据是什么。这样会很浪费时间，因为我们需要额外花费精力去辨认LLM回答的内容是否是“假情报”,这样还不如自己做呢。

因此使用RAG技术能很有效减少大模型幻觉，比如看看LLM回答时候引用的知识库，能确保他的回答是有根据的。

![image-20250108223341417](https://cdn.jsdelivr.net/gh/kashima19960/img@master/RAG%E5%92%8CLLM%E6%8A%80%E6%9C%AF%E6%90%AD%E5%BB%BA%E7%9F%A5%E8%AF%86%E5%BA%93/image-20250108223341417.png)

还有个我比较常用的是问一些很刁钻的知识点，其实也就是相当于让LLM帮我读书，然后整理好告诉我，毕竟这书写的，真的是抽象的我看不下去…..😐

比如下面这个问题,如果你没学过微机相关的内容，看不懂也没关系，理解我想表达的思想就行

```BASH
8253-5工作于方式2，用BCD码计数，用1号计数器，只读高8位则控制字为：\_\_\_\_\_。
 A．01010101B
 B．01000101B
 C．01100101B 
 D．01100100B
```

先看看claude 3.5 Sonnet(跟GPT4o一个梯队的)的回答

![image-20250108225543896](https://cdn.jsdelivr.net/gh/kashima19960/img@master/RAG%E5%92%8CLLM%E6%8A%80%E6%9C%AF%E6%90%AD%E5%BB%BA%E7%9F%A5%E8%AF%86%E5%BA%93/image-20250108225543896.png)

我直接说结论，这道题应该选 C，8253的方式选择控制字如下图，所以要达成题目的要求，对应控制字的二进制位应该设置为 `01100101B`。但是你看到claude 3.5 Sonnet的回答了吗？他给出的解释中，对应控制字位的功能完全就是瞎编的，而且还编的相当严谨，让你觉得有理有据，但其实这是**大模型幻觉**🤣

![image-20250108225752342](https://cdn.jsdelivr.net/gh/kashima19960/img@master/RAG%E5%92%8CLLM%E6%8A%80%E6%9C%AF%E6%90%AD%E5%BB%BA%E7%9F%A5%E8%AF%86%E5%BA%93/image-20250108225752342.png)

然后我们再对比一下用了RAG技术的回答，就能看到回答了正确的答案C，因为要是问8253的某个特定的控制字，只有查阅了书上的内容才知道的。

![image-20250108230552640](https://cdn.jsdelivr.net/gh/kashima19960/img@master/RAG%E5%92%8CLLM%E6%8A%80%E6%9C%AF%E6%90%AD%E5%BB%BA%E7%9F%A5%E8%AF%86%E5%BA%93/image-20250108230552640.png)

## 什么是RAG？

在上文多次提到了 RAG，那么 RAG 到底是什么？

RAG的全称是Retrieval **Augmented** Generation，也就是**检索，增强，生成**，由 数据提取——embedding（向量化）——创建索引——检索——自动排序（Rerank）——LLM归纳生成，以上部分组成。所以RAG就是通过检索获取相关的知识并将其融入Prompt，让大模型能够参考相应的知识从而给出合理回答。

下图是实现的原理，如果实在看不懂这个图也没啥关系。因为我们是使用者，直接找实现了RAG技术的项目来用就行了。

![实现原理](https://cdn.jsdelivr.net/gh/kashima19960/img@master/RAG%E5%92%8CLLM%E6%8A%80%E6%9C%AF%E6%90%AD%E5%BB%BA%E7%9F%A5%E8%AF%86%E5%BA%93/principle.jpg)

## 搭建过程

基于LLM+RAG的问答系统有很多，我这里推荐用开源的[MaxKB - 基于大模型和 RAG 的知识库问答系统 - 官网](https://maxkb.cn/index.html),官方文档：[快速入门 - MaxKB 文档](https://maxkb.cn/docs/quick_start/)关于安装方法和使用其实已经写的很详细了，但如果只是基本的使用的话，官方文档的很多东西是用不到的或者是小白根本就玩不明白的，这个看你自己的能力和需求

### 通过docker安装

论最简单的安装方法，我只推荐用docker，因为最无脑

Windows的话，下载docker desktop[Get Started | Docker](https://www.docker.com/get-started/)，下载后长这样，有图形化界面，用起来很简单

![image-20250108233843594](https://cdn.jsdelivr.net/gh/kashima19960/img@master/RAG%E5%92%8CLLM%E6%8A%80%E6%9C%AF%E6%90%AD%E5%BB%BA%E7%9F%A5%E8%AF%86%E5%BA%93/image-20250108233843594.png)

> Linux要自己下载docker engine这些，太麻烦了，自强吧🤗

然后确保自己的dockers desktop开启了，打开命令行输入这个命令

```bash
docker run -d --name=maxkb --restart=always -p 8080:8080 -v C:/maxkb:/var/lib/postgresql/data -v C:/python-packages:/opt/maxkb/app/sandbox/python-packages cr2.fit2cloud.com/1panel/maxkb
```

我简单解释一下 `-p`表示指定端口，`8080:8080`表示端口映射，前面的是本机的访问端口，可以改，后面的是容器的端口，不要动，比如可以这样改 `-p 4444:8080`，然后通过 `4444`端口访问就行，`-v`指定数据保存的位置，也是同理，`:`前面的路径你可以改，`:`后面的路径不要动，

拉取成功后在docker desktop的Containers选项卡会显示,先检查一下有没有在运行，这个容器很大，所以运行后需要一定的时间进行初始化，然后点击Port就能在浏览器打开了

![image-20250108234752754](https://cdn.jsdelivr.net/gh/kashima19960/img@master/RAG%E5%92%8CLLM%E6%8A%80%E6%9C%AF%E6%90%AD%E5%BB%BA%E7%9F%A5%E8%AF%86%E5%BA%93/image-20250108234752754.png)

有登录界面就说明安装成功了，默认的账户和密码如下

```bash
http://目标服务器 IP 地址:8080

默认登录信息
用户名：admin
默认密码：MaxKB@123..
```

![image-20250108235103601](https://cdn.jsdelivr.net/gh/kashima19960/img@master/RAG%E5%92%8CLLM%E6%8A%80%E6%9C%AF%E6%90%AD%E5%BB%BA%E7%9F%A5%E8%AF%86%E5%BA%93/image-20250108235103601.png)

### 创建知识库

查看上面的原理可以知道，做知识库首先要先将文档向量化，默认使用的那个向量模型的嵌入速度太慢了，所以我们需要配置**向量模型**，我这里推荐用百度的千帆大模型，因为新注册的用户可以白嫖一些额度，用来应付期末考试的复习就够用了

![image-20250108235540846](https://cdn.jsdelivr.net/gh/kashima19960/img@master/RAG%E5%92%8CLLM%E6%8A%80%E6%9C%AF%E6%90%AD%E5%BB%BA%E7%9F%A5%E8%AF%86%E5%BA%93/image-20250108235540846.png)

api key和secret key怎么配置，可以自己去[百度智能云控制台](https://console.bce.baidu.com/qianfan/overview)研究

![image-20250108235740080](https://cdn.jsdelivr.net/gh/kashima19960/img@master/RAG%E5%92%8CLLM%E6%8A%80%E6%9C%AF%E6%90%AD%E5%BB%BA%E7%9F%A5%E8%AF%86%E5%BA%93/image-20250108235740080.png)

然后还要配置语言模型，这里我也推荐用千帆大模型，因为api key和secret key跟向量模型的配置是一样的，当然用其他模型也行，这个自行查看对应的官方文档

![image-20250109000045379](https://cdn.jsdelivr.net/gh/kashima19960/img@master/RAG%E5%92%8CLLM%E6%8A%80%E6%9C%AF%E6%90%AD%E5%BB%BA%E7%9F%A5%E8%AF%86%E5%BA%93/image-20250109000045379.png)

创建一个知识库，然后上传文档

![image-20250109000432078](https://cdn.jsdelivr.net/gh/kashima19960/img@master/RAG%E5%92%8CLLM%E6%8A%80%E6%9C%AF%E6%90%AD%E5%BB%BA%E7%9F%A5%E8%AF%86%E5%BA%93/image-20250109000432078.png)

悬停到 `文件状态`会显示向量化的进度

![image-20250109000512901](https://cdn.jsdelivr.net/gh/kashima19960/img@master/RAG%E5%92%8CLLM%E6%8A%80%E6%9C%AF%E6%90%AD%E5%BB%BA%E7%9F%A5%E8%AF%86%E5%BA%93/image-20250109000512901.png)

### 创建应用

在应用那一栏创建应用，AI模型就是你配置的语言模型，知识库关联上面创建好的，自定义提示词建议别去碰，用默认的就好(血的教训)

![image-20250109000644897](https://cdn.jsdelivr.net/gh/kashima19960/img@master/RAG%E5%92%8CLLM%E6%8A%80%E6%9C%AF%E6%90%AD%E5%BB%BA%E7%9F%A5%E8%AF%86%E5%BA%93/image-20250109000644897.png)

到此搭建就完成了，完全能够满足个人的使用

## 参考资料

[大模型主流应用RAG的介绍——从架构到技术细节 | 我的学习笔记 | 土猛的员外](https://luxiangdong.com/2023/09/25/ragone/)

[开始使用 | Docker --- Get Started | Docker](https://www.docker.com/get-started/)

[系统架构 - MaxKB 文档](https://maxkb.cn/docs/system_arch/)
