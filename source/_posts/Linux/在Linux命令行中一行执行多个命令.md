---
title: 在Linux命令行中一行执行多个命令
date: 2024-10-22 21:42:00
tags: Linux
---
## 前言

在众多Linux教程中，我们常常可以看到详尽的知识点讲解和理论阐述，这对于初学者来说无疑是宝贵的资源。然而，在实际操作中，我们往往需要一些更为实用的技巧来提升工作效率。本文旨在填补这一空白，总结了一系列实用的Linux操作技巧，帮助你在日常使用中更加游刃有余。

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

### 如何进行选择

以上的三种方法都可以实现一行执行多个命令，但是他们之间的用法是有区别的，下面我简要概括一下每种方式的使用场景

1.   命令的执行的结果之间无逻辑关系，比如

```bash
ls -a .;ls -a /
```

这两个命令执行是否成功，都不会影响到彼此，因此这种情况下，使用分号(;)即可

2.   命令的执行的结果之间有逻辑关系

**假如后一个命令必须依赖前一个命令，这种情况下就使用`&&`**

比如

```bash
$ cat file.txt && ls -l file.txt
```

上面例子中，只有`cat`命令执行成功，才会继续执行`ls`命令。如果`cat`执行失败（比如不存在文件`flie.txt`），那么`ls`命令就不会执行。

**假如后一个命令是作为前一个命令的替补选择的话，这种情况就使用`||`**

比如

```
$ mkdir foo || mkdir bar
```

上面例子中，只有`mkdir foo`命令执行失败（比如`foo`目录已经存在），才会继续执行`mkdir bar`命令。如果`mkdir foo`命令执行成功，就不会创建`bar`目录了。