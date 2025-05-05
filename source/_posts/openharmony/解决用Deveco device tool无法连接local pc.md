---
title: 解决用Deveco device tool无法连接local pc
date: 2025-05-05 13:43:00
tags: openharmony
---

## 问题描述

Windows+Ubuntu 环境下DevEco tool upload Hi3681开发 烧录 Local PC 箭头红一下，又绿了

用Deveco device tool进行`upload`操作需要先连接这个local PC

![image-20250327105332856](https://cdn.jsdelivr.net/gh/kashima19960/img@master/openharmony/image-20250327105332856.png)

但是有的时候，这个Local PC你一直按![zh-cn_image_0000001275432904](https://cdn.jsdelivr.net/gh/kashima19960/img@master/openharmony/zh-cn_image_0000001275432904.png)都死活连不上。或者是变成![zh-cn_image_0000001326512673](https://cdn.jsdelivr.net/gh/kashima19960/img@master/openharmony/zh-cn_image_0000001326512673.png)后又立刻变成绿色按钮

## 解决方法

这种情况我去Openharmony找了很多解决方法，找到了一个能解决的方法

>   可以在设置那里改一下端口号，\*:\*改为确定的值 两边不要一样，比如 2221:3332

![image-20250505135251190](https://cdn.jsdelivr.net/gh/kashima19960/img@master/openharmony/image-20250505135251190.png)

具体可以参考以下的链接

[求助怎么解决Windows+Ubuntu 环境下DevEco tool upload Hi3681开发 烧录 Local PC 箭头红一下，又绿了-华为开发者问答 | 华为开发者联盟](https://developer.huawei.com/consumer/cn/forum/topic/0202106266891107671?fid=0103702273237500027)

