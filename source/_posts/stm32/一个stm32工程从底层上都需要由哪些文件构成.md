---
title: 一个stm32工程从底层上都需要由哪些文件构成
date: 2025-05-17 10:00:00
tags: stm32
---
## 前言

我最近因为做课设要用到stm32，所以去找了一些开源的stm32工程来看看，然后发现现在新版的keil mdk对于环境的配置跟以前	相比发生了较大的变化，比如我了解了一个叫RTE(real time envirement)，这个玩意可以帮你管理stm32的运行环境，比如标准库，CMSIS标准等等。但是我们中国的开发者入门单片机一般都会选择正点原子和野火这两家，他们这两家都是教你手动去构建一个工程，但是为了初学者，也同样是对工程的创建步骤做了一部分简化，比如把CMSIS文件夹的所需文件进行了裁剪。但是这些都有个很大的问题，开发环境是一直在变得，只要底层框架变了，你根本就不知道要怎么运行别人的项目，所以这篇文章我想写写，构成一个stm32工程都需要哪些文件，以及这些文件的作用都是什么

## STM32工程构建组成部分

用一句话概括STM32工程的构成部分就是，**CMSIS+库(可选)+启动文件+设备固件驱动文件+用户层**

正点原子是这样教你学怎么创建工程的

![1747495656289](https://cdn.jsdelivr.net/gh/kashima19960/img@master/stm32/1747495656289.png)

但是事实上，这些文件夹的划分都是自定义的，你在初学的时候，可以不需要知道里文件夹的文件的作用都是什么，根据教学的步骤一步步创建就行了，但是你要是用别人的开源工程就不行了，你必须得知道底层是由什么文件组成的，不然无法处理其中的依赖关系

![1747495666931](https://cdn.jsdelivr.net/gh/kashima19960/img@master/stm32/1747495666931.png)

所以我总结的观点就是，stm32的工程本质上就是各个. c 文件和 .h头文件是相互引用罢了，重要的不是架构而是原理。架构只是为了更方便管理而已。如果你想的话，把所有的文件都放在一个文件夹都是可以的，一样能编译，inc和src里面是HAL库的文件，我为了演示方便，没有把全部文件都放出来。

![1747496059736](https://cdn.jsdelivr.net/gh/kashima19960/img@master/stm32/1747496059736.png)

## CMSIS

CMSIS指的是ARM Cortex™ 微控制器软件接口标准(Cortex Microcontroller Software Interface Standard)，其提供与供应商无关的硬件抽象层，为处理器和外设实现一致，简单的软件接口，从而简化软件的重用、缩短微控制器新开发人员的学习过程并缩短新设备的上市时间。

我们知道不同厂家，比如TI，ST，Freescale，Nordic Semiconductor等不同半导体厂家都有基于Cortex M系列内核的MCU产品，但是这些MCU的外设却大不相同，外设的设计、接口、寄存器等都不一样，因此一个能够非常熟练对STM32进行开发的工程师很难快速地上手开发一款他不熟悉的，尽管是Cortex M内核的芯片。而CMSIS的目的是让不同厂家的Cortex M内核的MCU至少在内核层次上能够做到一定的一致性，提高软件移植的效率，而这就是CMSIS出现的最主要原因。

### CMSIS结构

这里简单介绍一下CMSIS的文件结构，CMSIS包含如下四个部分：

* **CMSIS-CORE**
  提供与 Cortex-M0、Cortex-M3、Cortex-M4、SC000 和 SC300 处理器与外围寄存器之间的接口
* **CMSIS-DSP**
  包含以定点（分数 q7、q15、q31）和单精度浮点（32 位）实现的 60 多种函数的 DSP 库
* **CMSIS-RTOS**
  用于线程控制、资源和时间管理的实时操作系统的标准化编程接口
* **CMSIS-SVD**
  包含完整微控制器系统（包括外设）的程序员视图的系统视图描述 XML 文件

### CMSIS框架

以下是CMSIS 5.x标准的软件架构图：

![1747496633074](https://cdn.jsdelivr.net/gh/kashima19960/img@master/stm32/1747496633074.png)

从上图可以看到，CMSIS 5.x软件架构主要分为以下三层： **应用代码层** 、**CMSIS软件层** 和  **微控制器层** ，其中 **CMSIS软件层** 起着承上启下的作用，一方面该层对微控制器层进行了统一的实现，屏蔽了不同厂商对Cortex-M系列微处理器核内外设寄存器的不同定义，另一方面又向上层的操作系统和应用层提供接口，简化了应用程序开发的难度，使开发人员能够在完全透明的情况下进行应用程序的开发。如果没有CMSIS标准，那么各个半导体公司可能会自己制定各自产品的库函数的命名规则，而这会使得软件在不同厂家芯片上的移植变得困难。也正是如此，CMSIS层的实现也相对复杂些。有关CMSIS更详细的介绍请访问[ARM官网](https://developer.arm.com/embedded/cmsis)。

### CMSIS在工程中的使用

我们以CMSIS 6.0为例(不同版本的CMSIS包会有差异，但是这里的思想都是共通的)，可以自行去官方网站下载，这个pack本质上是一个压缩包，可以直接解压看到里面的内容

![1747496703077](https://cdn.jsdelivr.net/gh/kashima19960/img@master/stm32/1747496703077.png)

```
.
├── Core
│   ├── Include
│   │   ├── a-profile
│   │   ├── m-profile
│   │   ├── cmsis_compiler.h
│   │   ├── cmsis_version.h
│   │   ├── core_ca.h
│   │   ├── core_cm0.h
│   │   ├── core_cm0plus.h
│   │   ├── core_cm1.h
│   │   ├── core_cm23.h
│   │   ├── core_cm3.h
│   │   ├── core_cm33.h
│   │   ├── core_cm35p.h
│   │   ├── core_cm4.h
│   │   ├── core_cm55.h
│   │   ├── core_cm7.h
│   │   ├── core_cm85.h
│   │   ├── core_sc000.h
│   │   ├── core_sc300.h
│   │   ├── core_starmc1.h
│   │   └── tz_context.h
│   ├── Source
│   │   └── irq_ctrl_gic.c
│   ├── Template
│   │   ├── ARMv8-M
│   │   ├── Device_A
│   │   └── Device_M
│   └── Test
├── Documentation
│   ├── html
│   ├── index.html
│   └── version.js
├── Driver
│   ├── DriverTemplates
│   ├── Include
│   └── VIO
└── RTOS2
    ├── Include
    └── Source
```

我们一般只需要用到 ` core/include` 文件夹里面的内容，其他都是一些可选的内容，教学文档，或模板工程，我这里都列出来，有兴趣可以看看

* **Core**: 存放 CMSIS-Core 相关文件。CMSIS-Core 提供了一个标准化的方式来访问 Cortex-M 和 Cortex-A 处理器的核心寄存器和外设。

  * `Include`: 包含核心的头文件。
    * `cmsis_compiler.h`: 提供编译器抽象层，使得代码可以兼容不同的编译器。 (Core/Include/cmsis_compiler.h)
    * `cmsis_version.h`: 定义 CMSIS 规范的版本信息。 (Core/Include/cmsis_version.h)
    * `core_*.h` (例如 `core_cm4.h`): 针对特定 Cortex-M/A 处理器核心的头文件，定义了核心寄存器和访问函数。 (Core/Include/core_cm4.h)
    * `a-profile/` 和 `m-profile/`: 分别包含针对 Arm A-Profile 和 M-Profile 架构的特定头文件。 (a-profile, Core/Include/m-profile)
  * `Source`: 包含核心的源文件，例如 `irq_ctrl_gic.c` 用于通用中断控制器 (GIC) 的中断控制。 (Core/Source/irq_ctrl_gic.c)
  * `Template`: 包含设备启动和系统配置的模板文件，供芯片供应商根据具体设备进行修改和适配。 (Core/Template)
  * `Test`: 包含用于验证 CMSIS-Core 实现的单元测试套件。 (Core/Test/README.md)
* **Documentation**: 存放 CMSIS 的文档。

  * `html/`: 包含 HTML 格式的详细文档。 (Documentation/html)
  * index.html: 文档的入口页面。 (Documentation/index.html)
  * `version.js`: 可能用于文档版本控制或显示。 (Documentation/version.js)
* **Driver**: 存放 CMSIS-Driver 相关文件。CMSIS-Driver 为微控制器外设定义了通用的 API 接口。

  * `DriverTemplates/`: 包含驱动程序的模板文件。 (Driver/DriverTemplates)
  * `Include/`: 包含驱动程序的 API 头文件 (例如 `Driver_USART.h`, `Driver_SPI.h`)。 (Driver/Include)
  * `VIO/`: 可能包含虚拟输入/输出 (VIO) 驱动的实现，用于在仿真或开发板上模拟 I/O 操作。 (Driver/VIO)
* **RTOS2**: 存放 CMSIS-RTOS2 相关文件。CMSIS-RTOS API 是一个通用的实时操作系统接口。

  * `Include/`: 包含 RTOS2 API 的头文件。 (RTOS2/Include)
  * `Source/`: 包含 RTOS2 API 的参考实现或适配层源码。 (RTOS2/Source)

第一个要添加的是core_xxx.h，xxx对应的是内核架构，以stm32f103为例，他的架构的Cortex-M3，就要把core_cm3.h添加到你的工程。  core_cm3.h这个包含的是一些ARM CORTEX-M3内核相关的函数和宏定义，例如核内寄存器定义、部分核内外设的地址等等，其对应的是core_cm3.c文件。不过我创建工程的时候为了图方便，都是全部加进去，这样以后换芯片的时候，就不需要重写添加相应架构的core_xxx.h了

![1747497666104](https://cdn.jsdelivr.net/gh/kashima19960/img@master/stm32/1747497666104.png)

第二个是跟编译器相关的，armclang，gcc这些都是编译器的名称，不同的编译器，你在点keil的构建工程时，是会用到不同的编译选项的，这个cmsis的头文件就是给keil提供这些参数

![1747497927589](https://cdn.jsdelivr.net/gh/kashima19960/img@master/stm32/1747497927589.png)

这两个是描述编译器的版本和其他内容的，也是必要的

![1747497939912](https://cdn.jsdelivr.net/gh/kashima19960/img@master/stm32/1747497939912.png)

当然，每个项目还可能会用很多进阶的功能，如果你编译的时候报错，就在CMSIS包搜一下，看这个功能在那个头文件，添加到工程就行

## 库(可选)

stm32现在的库一般有HAL库和标准库，为什么我说库是可选的呢？因为如果你想的话，完全可以用寄存器开发的方式，就是根据芯片手册，找到对应寄存器的基地址和偏移地址，给寄存器特定的位赋值来启动功能

![1747498397038](https://cdn.jsdelivr.net/gh/kashima19960/img@master/stm32/1747498397038.png)

但是我肯定是不会这么干的，这样做的好处是，直接对寄存器赋值，少了一大堆的函数调用和宏定义，在编译的时候会非常快，效率会更高，但是这样开发效率极低，开发效率低，那影响的就是我的寿命😑😑，所以我都是能用库就用库的

标准库跟设备固件驱动放在一起了，这里先不说设备固件驱动，我以前没用过标准库，后面去了解了才知道的

![1747498667247](https://cdn.jsdelivr.net/gh/kashima19960/img@master/stm32/1747498667247.png)

同样，这个DFP(Device Family Pack) pack能直接作为文件夹解压出来，`device/StdPeriph_Driver`这个文件夹就是标准库，你工程要用到哪里，就需要把这些库添加到自己的工程，同样的我这个人挺懒的，嫌麻烦，我一般都是全部添加进去🤗

![1747498767852](https://cdn.jsdelivr.net/gh/kashima19960/img@master/stm32/1747498767852.png)

这里文件的命名都是stm32f10x_xxxx，但是有一个misc.c文件**这个文件提供了外设对内核中的 NVIC(中断向量控制器) 的访问函数，在配置中断时，我们必须把这个文件添加到工程中。** 但是HAL库是没有这类文件的，因为HAL库都集成在一起了

HAL的添加方法跟标准库差不多，不过HAL库没跟设备固件包放在一起，你要自己单独下载[STMicroelectronics/stm32f1xx-hal-driver at 38d14024a9d3f6802506c3ec7a4308563760e54e](https://github.com/STMicroelectronics/stm32f1xx-hal-driver/tree/38d14024a9d3f6802506c3ec7a4308563760e54e)

## 启动文件

启动文件是一个核心文件，里面是使用汇编语言写好的基本程序，当STM32 芯片上电启动的时候，受限会执行这里的汇编程序，从而建立起来C 语言的运行环境，所以我们把这个文件称为启动文件。启动文件主要用来进行堆栈的初始化、中断向量表的定义和中断函数的定义。启动文件要引导进入系统 `main`函数，`Reset_Handler`中断处理函数是唯一被实现了的函数，其在系统启动时会被调用。以下就是 `Reset_Handler`实现的代码：

```asm
; Reset handler
Reset_Handler    PROC
                 EXPORT  Reset_Handler             [WEAK]
     IMPORT  __main
     IMPORT  SystemInit
                 LDR     R0, =SystemInit
                 BLX     R0
                 LDR     R0, =__main
                 BX      R0
                 ENDP

```

启动文件存放在设备固件包的 `Keil.STM32F1xx_DFP.2.4.1\Device\Source\ARM `目录下

![1747501917656](https://cdn.jsdelivr.net/gh/kashima19960/img@master/stm32/1747501917656.png)

启动文件有很多，你得从中挑选一个，对于f103系列来说，可能会用到的启动文件只有3个：

* startup_stm32f10x_ld.s：适用于 **小容量** 产品
* startup_stm32f10x_md.s：适用于 **中容量** 产品
* startup_stm32f10x_hd.s：适用于 **大容量** 产品

这里的容量指的是FLASH的大小，具体规格如下：

| 小容量     | 中容量      | 大容量  |
| ---------- | ----------- | ------- |
| 16K or 32K | 64K or 128K | >= 256K |

你就根据具体使用的stm32型号添加对应的启动文件就行

## 设备固件驱动文件

上面在讲标准库的时候提到了设备固件包，这个DFP固件包，不同版本，他的文件存放的目录可能有差异，这个你要具体点进你下载的固件包里面找找，

Include/
├── stm32f10x.h
└── system_stm32f10x.h
Source/
├── system_stm32f10x.c
└── ARM/
    ├── startup_stm32f10x_cl.s
    ├── startup_stm32f10x_hd_vl.s
    ├── startup_stm32f10x_hd.s
    ├── startup_stm32f10x_ld_vl.s
    ├── startup_stm32f10x_ld.s
    ├── startup_stm32f10x_md_vl.s
    ├── startup_stm32f10x_md.s
    ├── startup_stm32f10x_xl.s
    └── STM32F1xx_OPT.s
StdPeriph_Driver/

然后设备驱动这里我们需要三个文件，`stm32f10x.h`,`system_stm32f10x.h`,`system_stm32f10x.c`

system_stm32f10x.c文件里面主要是系统时钟初始化函数SystemInit 相关的定义，一般情况下文件用户不需要修改。

`stm32f10x.h` 是 STM32F1 系列微控制器的顶层通用头文件，定义了各种寄存器以及外设的基地址和偏移地址

但是需要注意的是这个文件在CMSIS 5与CMSIS 6产生了巨大的变化

在CMSIS 5中是采用 `stm32f1xx.h`(注意看命名)加上具体芯片型号的头文件的形式

![1747504038709](https://cdn.jsdelivr.net/gh/kashima19960/img@master/stm32/1747504038709.png)

`stm32f1xx.h` 根据不同的宏定义，将具体型号的的头文件包含进去

![1747504089559](https://cdn.jsdelivr.net/gh/kashima19960/img@master/stm32/1747504089559.png)

但是在 CMSIS 6 中，STMicroelectronics 对设备头文件的结构进行了简化和统一，不再为每个具体型号提供单独的头文件，如 `stm32f103xe.h`。取而代之的是，使用通用的 `stm32f10x.h` 文件，并通过RTE的方式进行管理

![1747504342221](https://cdn.jsdelivr.net/gh/kashima19960/img@master/stm32/1747504342221.png)

如果你不使用RTE的话，你就要手动定义一下相应设备的宏，具体要选哪个，你可以点进去头文件查看，里面注释是写的很清楚的，不过是用的英文，你英文不好的话，就用一下翻译器

![1747504442629](https://cdn.jsdelivr.net/gh/kashima19960/img@master/stm32/1747504442629.png)

## 用户层

用户层就是你自己写的文件，main.c之类的，但是编译的时候，只有当上面的内容的文件都处理完，才会真正运行到你编写的main函数，所以你理解了吧，一个项目从配置到真正运行，是需要非常复杂的步骤的

## 总结

看完这个文章你就明白构成stm32工程是由 **CMSIS+库(可选)+启动文件+设备固件驱动文件+用户层 **的意思了，
但是随着版本的更替，固件包的使用方法也是会更替的，不过你只要懂了这个思想，不管怎么更替你都能处理好文件依赖，更何况现在有了RTE这个东西，文件的管理会更方便了，以后开发环境的使用对用户来说只会更友好。

这是正点原子的文件架构，虽然里面有些细节都是老版本，已经不适用于新的开发环境了，但是思想是不变的

![1747505133648](https://cdn.jsdelivr.net/gh/kashima19960/img@master/stm32/1747505133648.png)

## 参考资料

1. [最新版MDK5.41联合STM32CubeMX差点将MDK经典的RTE用法折腾完犊子，堪称2025最强坑王组合 - 开发环境 - 硬汉嵌入式论坛 - Powered by Discuz!](https://www.armbbs.cn/forum.php?mod=viewthread&tid=127684)
2. [【STM32学习笔记】（4）—— STM32工程文件详解_stm32工程文件结构-CSDN博客](https://blog.csdn.net/qq_53918631/article/details/125075661)
3. [STM32不同型号的芯片对应的启动文件如何选择_stm32启动文件与芯片对心-CSDN博客](https://blog.csdn.net/weixin_44788542/article/details/111645556)
4. [一个完整的STM32工程到底由哪些文件组成_stm32工程文件夹如何分类-CSDN博客](https://blog.csdn.net/sinat_16643223/article/details/107174897)
5. [【STM32】使用RTE ，从 0 开始创建一个 (keil) ARM MDK工程（纯keil，标准库，以STM32F103C8T6为例）_keil ](https://blog.csdn.net/weixin_43764974/article/details/131754334)
6. [导入限制 | Embedded IDE For VSCode](https://em-ide.com/zh-cn/docs/notice/keil_project_limit/)rte-CSDN博客
