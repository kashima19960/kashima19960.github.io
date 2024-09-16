---
title: 掌握这些Linux实用技巧，让你操作更高效！
date: 2024-08-07 20:00:00
tags: Linux
---
## 前言

在众多Linux教程中，我们常常可以看到详尽的知识点讲解和理论阐述，这对于初学者来说无疑是宝贵的资源。然而，在实际操作中，我们往往需要一些更为实用的技巧来提升工作效率。本文旨在填补这一空白，总结了一系列实用的Linux操作技巧，帮助你在日常使用中更加游刃有余。

## Bash快捷键

- 编辑命令

    * Ctrl + a ：移到命令行首
    * Ctrl + e ：移到命令行尾
    * Ctrl + f ：按字符前移（右向）
    * Ctrl + b ：按字符后移（左向）
    * **Alt + f ：按单词前移（右向）**
    * **Alt + b ：按单词后移（左向）**
    * Ctrl + xx：在命令行首和光标之间移动
    * Ctrl + u ：从光标处删除至命令行首
    * **Ctrl + k ：从光标处删除至命令行尾**
    * **Ctrl + w ：从光标处删除至字首**
    * Alt + d ：从光标处删除至字尾
    * Ctrl + d ：删除光标处的字符
    * Ctrl + h ：删除光标前的字符
    * Ctrl + y ：粘贴至光标后
    * Alt + c ：从光标处更改为首字母大写的单词
    * Alt + u ：从光标处更改为全部大写的单词
    * Alt + l ：从光标处更改为全部小写的单词
    * Ctrl + t ：交换光标处和之前的字符
    * Alt + t ：交换光标处和之前的单词
    * Alt + Backspace：与 Ctrl + w 类似，分隔符有些差别

----

- 重新执行命令

    * Ctrl + r：逆向搜索命令历史
    * Ctrl + g：从历史搜索模式退出
    * Ctrl + p：历史中的上一条命令
    * Ctrl + n：历史中的下一条命令
    * Alt + .：使用上一条命令的最后一个参数

----

- 控制命令

    * Ctrl + l：清屏
    * Ctrl + o：执行当前命令，并选择上一条命令
    * Ctrl + s：阻止屏幕输出
    * Ctrl + q：允许屏幕输出
    * Ctrl + c：终止命令
    * Ctrl + z：挂起命令

----

- Bang (!) 命令

    * !!：执行上一条命令
    * !blah：执行最近的以 blah 开头的命令，如 !ls
    * !blah:p：仅打印输出，而不执行
    * !$：上一条命令的最后一个参数，与 Alt + . 相同
    * !$:p：打印输出 !$ 的内容
    * !*：上一条命令的所有参数
    * !*:p：打印输出 !* 的内容
    * ^blah：删除上一条命令中的 blah
    * ^blah^foo：将上一条命令中的 blah 替换为 foo
    * ^blah^foo^：将上一条命令中所有的 blah 都替换为 foo

## 一行执行多个命令

问题：用apt安装软件的时候，你肯定都会先更新软件源，然后再安装软件，有没有方法可以在一行做到呢？

有三种方式可以做到这个操作

1. [ ; ]

特点：如果被分号(;)所分隔的命令会连续的执行下去，就算是错误的命令也会继续执行后面的命令。

```bash
[root@localhost etc]# lld ; echo "ok" ; lok
-bash: lld: command not found
ok
-bash: lok: command not found
```

2. [ && ]

特点：如果命令被 && 所分隔，那么命令也会一直执行下去，但是中间有错误的命令存在就不会执行后面的命令，没错就直行至完为止。
```bash
[root@localhost etc]# echo "ok" && lld && echo "ok"
ok
-bash: lld: command not found
```
3. [ || ]

特点：如果每个命令被双竖线 || 所分隔，那么一遇到可以执行成功的命令就会停止执行后面的命令，而不管后面的命令是否正确与否。如果执行到错误的命令就是继续执行后一个命令，一直执行到遇到正确的命令为止。
```bash
[root@localhost etc]# echo "ok" || echo "haha"
ok
[root@localhost etc]# lld || echo "ok" || echo "haha"
-bash: lld: command not found
ok
```

那么回到最初的问题，在一行更新并安装软件可以用下面的方式做到
```bash
sudo apt update;sudo apt install software
```