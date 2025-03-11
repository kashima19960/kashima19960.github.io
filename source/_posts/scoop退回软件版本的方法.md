---
title: scoop退回软件版本的方法

date: 2025-3-11 23:53:00

tags: 其他
---
## 前言

在软件更新后，如果出现了很影响使用体验的问题，那么可以把软件先退回以前的版本进行使用，

但是scoop本身并没有提供直接让软件回退版本的功能，因此这篇文章我教大家如何做到回退软件版本

## 具体方法

scoop安装软件是通过bucket中的json文件实现的，它的路径是 `scoop\buckets\main\bucket`,这个文件夹包含了当前软件库中的所有软件的描述信息(感兴趣有啥内容可以自己打开来看)

然后每个软件库都是一个git仓库，所以我们可以用git操作来使得软件库退回到特定的版本

我们拿extras仓库举例(路径是`scoop\buckets\extras`)，通过git仓库找到vscode的旧版本

首先我们得找到特定版本的`commit hash`值，这个操作可以用`git log -S"关键词"`实现
所以我们可以通过命令行在软件库使用`git log -S"vscode"`查找到与vscode有关的提交信息
当然，如果你有会使用的git图形化工具，那也是可以的
```bash
commit fb6af57934c019ca66e4126be7cc44bb025a42a3
Author: Ilja Nosik <ilja.nosik@outlook.com>
Date:   Fri Sep 9 11:35:53 2016 +0200

    Update VS Code to 1.5.1 (#266)

    * Update VS Code to 1.5.1

    * Check the version of VS Code at GitHub
```
注意到这个的提交信息是`Update VS Code to 1.5.1`,这就是我们要找的，把commit的后面的哈希值复制出来

然后`git checkout fb6af57934c019ca66e4126be7cc44bb025a42a3`,这样我们就能把git仓库暂时回退到这个版本。进入`\scoop\buckets\extras\bucket`这个文件夹，把`vscode.json`这个文件,复制出来。
成功之后，要记得用`git checkout master`将软件库复原

最后使用`scoop install vscode.json`安装指定版本的vscode

## 结语
通过以上的操作,其实你只要理解了scoop安装软件是通过一个json文件实现的，就知道如何安装特定版本的软件