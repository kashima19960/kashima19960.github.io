---
title: Vscode运行Python无法导入自己编写的包的解决方法
date: 2024-9-13 17:34:00
tags: 其他
---
## 前言

 我写python代码，大多数时间都是使用vscode编辑器，一般而言，在导入第三方包或者是Python内置的包，基本上都不会遇到什么问题。然而，当我尝试导入一个**跨文件**自定义的包时，却遭遇了导入异常的问题，因此我写下这篇文章是记录我解决这个问题的方法与思路，希望通过分享解决这一问题的方法，帮助遇到类似问题的开发者。以及我觉得“包”这个称呼，不太贴切我们日常使用操作系统的习惯，因此后面我都会称呼为“文件夹”。

## 作者所使用的平台

- **Vscode编辑器**
- **python3.8.10**
- **venv虚拟环境**

## 存在的问题

导入模块时，可以看到编辑器并没有给出任何的报错

![image-20240913165159066](https://raw.githubusercontent.com/kashima19960/img/master/Vscode%E8%BF%90%E8%A1%8CPython%E6%97%A0%E6%B3%95%E5%AF%BC%E5%85%A5%E8%87%AA%E5%B7%B1%E7%BC%96%E5%86%99%E7%9A%84%E5%8C%85%E7%9A%84%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95%20/image-20240913165159066.png)

但是运行 `cluster.py`的时候，出现了下面的错误

```shell
Traceback (most recent call last):
  File "d:\z资料\s数学建模\MathModels\Models\cluster.py", line 6, in <module>
    from DataProcess.decomposer import PCA
ModuleNotFoundError: No module named 'DataProcess'
```

通过查看文件树，可以看到 `DataProcess` 是一个文件夹，`cluster.py`所在的文件夹 `Models`与 `DataProcess`文件夹是属于同级文件夹

![image-20240913152248415](https://raw.githubusercontent.com/kashima19960/img/master/Vscode%E8%BF%90%E8%A1%8CPython%E6%97%A0%E6%B3%95%E5%AF%BC%E5%85%A5%E8%87%AA%E5%B7%B1%E7%BC%96%E5%86%99%E7%9A%84%E5%8C%85%E7%9A%84%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95%20/image-20240913152248415.png)

这里有个知识点，是你必须知道的，Python在导入包的时候，会对包所在的路径进行搜索，并且这个搜索是有优先级的

1. **当前目录**：Python首先检查当前的工作目录。
2. **PYTHONPATH**：这是环境变量，包含了一系列目录路径，Python会在此查找。
3. **安装的第三方库**：Python会检查在site-packages目录下的第三方库。
4. **Python标准库**：最后，Python会检查内置的标准库。

这个顺序确保了本地目录的优先级最高，然后是用户自定义的路径，接着是第三方库，最后是Python的标准库。这样做可以避免本地目录下的模块与标准库或第三方库中的模块发生命名冲突。

从上面的优先级可以看到，我们之所以会出现 `ModuleNotFoundError: No module named 'DataProcess'`，是因为我们导入的包的位置不符合上述四个当中的任意一个，因此Python解释器在解释代码的时候就无法找到我们自定义的包。

## 解决的方法

根据上述讲到的问题，我们简单分析一下，既然Python解释器无法找到我们自定义的包，那么就由我们自己告诉Python解释器，我们自定义的包在什么地方不就行了？😈😈这里可以使用 `.pth`文件来手动指定Python搜索包的路径

> 在Python中，.pth文件是一种文本文件，它包含了一行一行的目录路径。这些路径会被Python解释器识别，并将其添加到模块搜索路径中。通过使用.pth文件，我们可以轻松地自定义Python模块的路径，方便地添加第三方库或自己编写的模块。所以.pth文件就提供给了我们除了上面四种搜索方法的额外拓展的办法。

1. 找到site-packages文件夹

这个文件夹一般是用来存放第三方库的位置，我们可以利用这个文件夹，他通常都会在python解释器的Lib目录下，比如本文用的是venv虚拟环境，这个文件夹都位于 `.venv\Lib\site-packages`

2. 在site-packages文件夹下新建一个mypath.pth文件

注：这个文件名是任取的，不一定非得叫mypath

3. 在mypath.pth文件写入自定义包的路径

拿我自己的项目举例，你只需要在mypath.pth文件中填写**项目根目录文件夹的路径**就行了，如下图所示

ps:这里推荐用绝对路径，当然用相对路径也是可以的

![image-20240913165342658](https://raw.githubusercontent.com/kashima19960/img/master/Vscode%E8%BF%90%E8%A1%8CPython%E6%97%A0%E6%B3%95%E5%AF%BC%E5%85%A5%E8%87%AA%E5%B7%B1%E7%BC%96%E5%86%99%E7%9A%84%E5%8C%85%E7%9A%84%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95%20/image-20240913165342658.png)

在这里有一个非常容易出现的误区，有些人可能会心想，既然导入的是DataProcess包(文件夹)，那么为什么不直接填写DataProcess包(文件夹)的路径呢(如下图所示)？事实上，这种想法是错误的，在路径搜索中python解释器会将一个包(文件夹)当成一个整体看待，因此你给出的路径得是这个包的根目录才行。

![image-20240913155109563](https://raw.githubusercontent.com/kashima19960/img/master/Vscode%E8%BF%90%E8%A1%8CPython%E6%97%A0%E6%B3%95%E5%AF%BC%E5%85%A5%E8%87%AA%E5%B7%B1%E7%BC%96%E5%86%99%E7%9A%84%E5%8C%85%E7%9A%84%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95%20/image-20240913155109563.png)

## 运行结果

一切都顺利的话，我们再次重新运行 `cluster.py`，应该就不会再次出现导入出错的情况了

![success](https://raw.githubusercontent.com/kashima19960/img/master/Vscode%E8%BF%90%E8%A1%8CPython%E6%97%A0%E6%B3%95%E5%AF%BC%E5%85%A5%E8%87%AA%E5%B7%B1%E7%BC%96%E5%86%99%E7%9A%84%E5%8C%85%E7%9A%84%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95%20/success.png)

如何你执行完以上的步骤后，仍然会导入异常，可能有以下的原因

- 缓存没有清空
- .pth文件放错位置了
- 路径没有写对

可以尝试清空缓存试试,按下 `ctrl+shift+p`，输入python，找到下面的选项

![image-20240913171701496](https://raw.githubusercontent.com/kashima19960/img/master/Vscode%E8%BF%90%E8%A1%8CPython%E6%97%A0%E6%B3%95%E5%AF%BC%E5%85%A5%E8%87%AA%E5%B7%B1%E7%BC%96%E5%86%99%E7%9A%84%E5%8C%85%E7%9A%84%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95%20/image-20240913171701496.png)
