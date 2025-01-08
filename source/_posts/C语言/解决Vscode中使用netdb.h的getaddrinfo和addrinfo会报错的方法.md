---
title: 解决Vscode中使用netdb.h的getaddrinfo和addrinfo会报错的方法
date: 2024-12-03 23:14:00
tags: C语言
---

## 前言

博主最近在学习c语言的socket编程，在调用netdb.h中的相关函数和变量api时，遇到了一些问题，因此本文将给出解决的方法，并且进行分析

### 博主的配置

-   wsl：ubuntu20.04发行版
-   vscode：1.95.3

## 问题的描述

使用addrinfo(属于netdb.h头文件)结构体变量的时候，vscode会报错

![image-20241203234701125](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/image-20241203234701125.png)

调用getaddrinfo()函数的时候，vscode也索引不到这个函数的定义

![image-20241203234754622](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/image-20241203234754622.png)

其实这个函数就位于netdb.h中，可以看到，这一部分是灰色的

![image-20241203234937711](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/image-20241203234937711.png)

但是使用gcc编译的时候，是能够正确编译链接的，说明程序是没有语法和语义错误的

![image-20241203235130147](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/image-20241203235130147.png)

因此我推测是vscode的c语言扩展的intellisense智能提示的问题，就是下图的这个扩展(不得不说微软的东西，屁事就是多😅)

![image-20241203235234757](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/image-20241203235234757.png)

## 解决的方法

我查阅了很多资料，最终也是找到了解决的方法。我的风格就是先告诉你怎么做，解决你的燃眉之急，至于为什么要这么做，之后我再娓娓道来😋所以如果你对原因分析不感兴趣的话，后面的分析和总结你可以跳过不看❤️

### 方法1：在插件设置中更改c standard

进入c/c++插件的设置中，找到这一栏

![image-20241204000236168](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/image-20241204000236168.png)

然后将c99修改成gnu的c语言标准，我试过了，修改成GNU的任意一个都行

![image-20241204000400301](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/image-20241204000400301.png)

可以看到已经不会报错了

![image-20241204000455795](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/image-20241204000455795.png)

### 方法2：定义_GNU_SOURCE

在代码文件中添加`_GNU_SOURCE`的宏定义

```c
#define _GNU_SOURCE
```

或者在.vscode中新建一个`c_cpp_properties.json`,然后在这个文件中定义这个宏，我个人推荐这个做法，因为修改配置文件能作用于整个工程,上面那种只能作用于单个文件。

```json
{
    "configurations": [
        {
            "name": "Linux",
            "includePath": [
                "${workspaceFolder}/**"
            ],
            "compilerPath": "/usr/bin/gcc",
            "cStandard": "${default}",
            "intelliSenseMode": "${default}",
            "defines": [
                "_GNU_SOURCE"
            ]
        }
    ],
    "version": 4
}
```

## 分析与总结

现在来分析一下为什么会报错，造成报错的原因是什么。然后总结一下

### 原因分析

先说结论：**netdb.h属于GNU 特有扩展**

标准的c语言本身并不直接包含对`netdb.h`的支持，所以你现在明白为啥上面打开netdb.h文件后发现有一部分是灰色(说明没有被包含)了吧。

那么GNU的c标准，和普通的c标准有啥区别呢？简单来说就是在普通的c标准上加了很多扩展功能,`netdb.h`就是GNU特有扩展功能的一部分，所以解决方案2就是这么来的，将c standard切换成GNU C就行了

| 特性     | C99                      | GNU99                                     |
| -------- | ------------------------ | ----------------------------------------- |
| 标准     | 遵循 ISO C99 标准        | C99 加上 GNU 扩展                         |
| 扩展     | 不支持 GNU 特有扩展      | 支持 GNU 特有扩展                         |
| 兼容性   | 严格遵循标准             | 允许使用非标准的 GNU 特性                 |
| 默认设置 | 不定义 `__STRICT_ANSI__` | 定义`__STRICT_ANSI__` 以禁用所有 GNU 扩展 |

>   -   **[C99](https://zh.wikipedia.org/wiki/C99)**: 这是 1999 年发布的 C 语言标准（ISO/IEC 9899:1999）。它引入了许多新特性，如布尔类型、复合字面量、可变参数宏等。使用 `c99` 编译器选项时，代码将遵循这一标准。
>   -   **GNU99**: 这是基于 C99 标准的 GNU 扩展版本。使用 `gnu99` 选项时，除了 C99 的特性外，还可以使用 GNU 编译器（GCC）提供的一些额外功能和扩展。这些扩展可能包括额外的语法和库函数，这些在标准 C 中并不被支持。



那么`_GNU_SOURCE`这个宏又是哪来的？干嘛的？

>    _GNU_SOURCE是一个宏定义，用于启用GNU C库（glibc）中的许多非标准扩展和功能。定义这个宏后，程序可以访问一些POSIX标准中未包含的传统功能以及GNU/Linux特有的扩展接口。

所以当你定义了这个宏的时候，那么下面标准的所有功能都会启用：ISO C89、ISO C99、POSIX.1、POSIX.2、BSD、SVID、X/Open、LFS 以及 GNU 扩展。在 POSIX.1 与 BSD 发生冲突的情况下，POSIX 定义优先。

这就是解决方案1的由来，定义了这个宏之后就能启用GNU的扩展

### 总结

有一种说法是写程序都是三分在写，七分在调，我觉得说的很对，写程序最重要的反而不是编写代码，而是如何去调试代码，解决报错，总结问题，我在解决本文的问题的时候，上网查阅了很多资料，以前我并不会去在意C语言不同标准带来的差异，因为写的程序能跑就行😋。但是当你解决问题的时候会发现，你可能会接触到别人写的资料中不胜其烦的枯燥术语，难以理解的代码逻辑，当你经历这个过程后，你的code能力就提升了。

## 参考资料

-   [C99 和 GNU99 的区别 - Undefined443 - 博客园](https://www.cnblogs.com/Undefined443/p/18468828)
-   [c - What does "#define _GNU_SOURCE" imply? - Stack Overflow](https://stackoverflow.com/questions/5582211/what-does-define-gnu-source-imply)
-   [关于__GNU_SOURCE 这个宏 - 颠覆者 - 博客园](https://www.cnblogs.com/raozhiyi/articles/9509600.html)
-   [Incomplete type error on struct addrinfo · Issue #2025 · microsoft/vscode-cpptools](https://github.com/microsoft/vscode-cpptools/issues/2025)