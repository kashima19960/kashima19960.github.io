---
title: QtDesign预览的效果与程序运行结果不一致的解决方法
date: 2024-10-09 21:52:00
tags: 其他
---
## 存在的问题

使用Qt designer软件设计出来的界面，与转换成python程序运行出来的结果不一致，具体看下图

### Qt designer预览结果

![image-20241009215433588](https://cdn.jsdelivr.net/gh/kashima19960/img@master/QtDesign%E9%A2%84%E8%A7%88%E7%9A%84%E6%95%88%E6%9E%9C%E4%B8%8E%E7%A8%8B%E5%BA%8F%E8%BF%90%E8%A1%8C%E7%9A%84%E7%BB%93%E6%9E%9C%E4%B8%8D%E4%B8%80%E8%87%B4%E7%9A%84%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95/image-20241009215433588.png)

### 程序运行出来的结果

![image-20241009215458231](https://cdn.jsdelivr.net/gh/kashima19960/img@master/QtDesign%E9%A2%84%E8%A7%88%E7%9A%84%E6%95%88%E6%9E%9C%E4%B8%8E%E7%A8%8B%E5%BA%8F%E8%BF%90%E8%A1%8C%E7%9A%84%E7%BB%93%E6%9E%9C%E4%B8%8D%E4%B8%80%E8%87%B4%E7%9A%84%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95/image-20241009215458231.png)

## 原因分析

我自己的电脑是2560*1600分辨率的屏幕，采用的是200%的缩放比例，出现这种情况是因为Windows的在高dpi下的老毛病了，常见的现象就是应用程序的各个组件缩放不正常。什么是高dpi这里不做探讨，有兴趣的读者可以自己去了解。

## 解决方法

在程序中加入这一行代码，它的作用是启动应用程序的高dpi缩放

```python
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
```

### 结果

![image-20241009220239777](https://cdn.jsdelivr.net/gh/kashima19960/img@master/QtDesign%E9%A2%84%E8%A7%88%E7%9A%84%E6%95%88%E6%9E%9C%E4%B8%8E%E7%A8%8B%E5%BA%8F%E8%BF%90%E8%A1%8C%E7%9A%84%E7%BB%93%E6%9E%9C%E4%B8%8D%E4%B8%80%E8%87%B4%E7%9A%84%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95/image-20241009220239777.png)

### 常见误区

请勿用以下的方法启动高dpi缩放，高dpi缩放必须在app创建之前启动

```python
app = QtWidgets.QApplication(sys.argv)
app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling,True)

'''
程序会出现以下的提示
Attribute Qt::AA_EnableHighDpiScaling must be set before QCoreApplication is created.
'''
```

