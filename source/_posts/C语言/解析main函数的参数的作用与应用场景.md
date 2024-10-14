---
title: 解析main函数的参数的作用与应用场景
date: 2024-10-14 22:21:10
tags: C语言
---

## 前言

刚学习C语言的你，多数都会使用ide，比如visual studio等等，一般生成的代码模板都是这样的

```c
#include <stdio.h>
int main(int argc, char const *argv[])
{
    /* code */
    return 0;
}
```

通常来说`int argc, char const *argv[]`，用ide点点按钮编译文件的话，这两个参数你是用不到的，但是你难道没有好奇过这两个参数有啥用吗😕。今天我就简单解析一下这两个参数的作用与应用场景

## 定义与解析

百度百科是这样定义这两个参数的

>   **ARG**c和**ARG**v中的**ARG**指的是**"**参数**"**（外语：**ARG***uments, argument counter 和 argument vector* ） [1]
>
>   至少有两个[参数](https://baike.baidu.com/item/参数/5934974?fromModule=lemma_inlink)至[主函数](https://baike.baidu.com/item/主函数/8428535?fromModule=lemma_inlink)：ARGc和ARGv；
>
>   第一个是提供给主函数的参数个数，
>
>   第二个是参数的字符串数组的指针。 [1]

我给你翻译成人话，`argc`是指从命令行传入参数的个数，`argv`是参数名字的数组

举个例子你马上就懂了

假如有下面的代码main.c

```c
#include <stdio.h>
int main(int argc, char *argv[])
{
    // argc 是参数的数量
    // argv 是参数的列表，argv[0] 是程序名
    for (int i = 0; i < argc; i++)
    {
        printf("参数%d是: %s\n", i, argv[i]);
    }
    return 0;
}
```

然后我们用gcc进行编译，gcc是编译c语言的编译器，如果你没用过，没关系，先放着

```bash
# 我简单解释一下，-o表示指定编译后的程序名字为main.exe 
gcc main.c -o main.exe
```

然后我们在命令行执行main.exe

```bash
# 必须加上 ./ 不然命令行无法找到main.exe的路径(./ 表示当前路径)
./main.exe 111 222 333
```

之后就是重要部分了，在程序执行后，我们加上了三个数字111 222 和333，这里有三个数字，所以argc=3，argv=[“D:\coding\workspace\C_CPP\study\main.exe”,”111”,”222”,”333”]

运行结果如下

```c
参数 0是: D:\coding\workspace\C_CPP\study\main.exe
参数 1是: 111
参数 2是: 222
参数 3是: 333
```

argc=3,意思就是传进的参数有 3 个，那为什么argv数组有四个元素呢？

**argv[0]默认是程序的存放路径，这个记住就**行

最后有一个点要说一样，main函数的参数不一定非要要叫argc和argv，而是可以自定义的，所以你写成a和b都可以,argc和argv是约定成俗的一个名字。

```c
#include <stdio.h>

int main(int a, char *b[])
{
    // argc 是参数的数量
    // argv 是参数的列表，argv[0] 是程序名
    for (int i = 0; i < a; i++)
    {
        printf("参数 %d是: %s\n", i, b[i]);
    }
    return 0;
}
```



## 应用

看完上面的内容，你估计有个疑问，这玩意好像没啥用啊？

别急，我给你说一个例子你就懂了

假设你开发了一个命令行工具 **app.exe**  ,他的作用是对txt文件进行处理(具体是什么功能省略)

你可以这样写程序

```c
#include <stdio.h>

int main(int argc, char *argv[])
{
    printf("我要处理的文件是%s!",argv[1]);
    return 0;
}
```

然后你就可以这样使用，来把你要处理的文件名通过命令行传输进去，这样程序就能知道你要对那个文件进行操作。

```bash
D:\coding\workspace\C_CPP\study>.\app.exe file.txt
我要处理的文件是file.txt!
```

当然这只是一个简单的例子，以后学习Linux的时候，你会接触到更多这方面的使用。