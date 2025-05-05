---
title: 解决用vscode编写openharmony代码时，跳转函数定义和实现时间过长
date: 2025-03-21 20:03:00
tags: openharmony
---

## 问题描述

遇到过用Vscode在openharmony工程中编写代码时，智能提示会很慢，比如跳转函数定义和函数实现的时间非常长

## 问题分析

在中文互联网搜索这个问题，基本上找不到答案，所以我去stack overflow和github上找了很多文章，最终是找到了问题所在

这两篇文章描述了具体的原因

-   [C++智能感知和解析超级慢：r/vscode --- C++ intellisense and parsing SUPER slow : r/vscode](https://www.reddit.com/r/vscode/comments/l5hz4i/c_intellisense_and_parsing_super_slow/)

-   [在大型代码库中，C/C++的智能感知（IntelliSense）非常缓慢（由于填充文件名缓存）· #12169 号问题 · microsoft/vscode-cpptools --- C/C++ intellisense extremely slow with large codebases (due to populating file name cache) · Issue #12169 · microsoft/vscode-cpptools](https://github.com/microsoft/vscode-cpptools/issues/12169)

不想看的话，我总结一下，其实就是Vscode的c/c++扩展的问题

![image-20250321201200846](https://cdn.jsdelivr.net/gh/kashima19960/img@master/openharmony/image-20250321201200846.png)

这个扩展是微软官方给c/c++语言提供智能提示写的，它的工作原理是每次打开代码项目的时候就进行索引一次，如果代码库文件很少的话，倒是没啥问题，也能很快，但是如果像Openharmony这种源码超过了20多G的代码库，每次打开都进行索引的话，就会非常慢，所以就会导致跳转函数定义和函数实现的时间非常长

## 解决方法

解决问题最好的方法就是把问题的来源解决掉，所以我们直接不用这个微软的C/C++扩展就好了🤓。这里推荐用Clangd，clangd是不包含代码格式化和代码调试的，所以最好装上clang-Format和CodeLLDB

1.   最好要生成编译数据库compdb(compile database)，不要每次打开都索引代码 
2.    对于小项目，c/c++(微软官方的插件)毫无障碍 
3.    对于大工程，生成compile_commands.json文件，使用clangd(一种语言服务器,作用是代码补全，高亮关键字，函数跳转)扫描该文件并为当前项目中的源码生成索引。 
4.    由于clangd与c/c++会产生冲突，因为在编写Openharmony代码的时候无法使用c/c++所提供的代码格式化程序，因为这里采用clang-format进行平替，其中将格式化style设置为"WebKit"

![image-20250321202012919](https://cdn.jsdelivr.net/gh/kashima19960/img@master/openharmony/image-20250321202012919.png)

![image-20250321202130068](https://cdn.jsdelivr.net/gh/kashima19960/img@master/openharmony/image-20250321202130068.png)

## 具体配置方法

配置过程，会涉及一些ninja编译构建系统的内容，如果你不懂的话，就按照我给的步骤照做

核心就是生成一个compile_commands.json的文件，这个文件的作用如下

>   compile_commands.json 是一个编译数据库文件，包含了 OpenHarmony 项目中每个源文件的详细编译配置信息，主要用途有：
>
>   1. **提供代码智能分析基础** - 使 VS Code、Clangd 等工具能正确理解代码结构和依赖关系
>   2. **跨开发环境一致性** - 确保不同开发者使用相同的编译参数和头文件路径
>   3. **静态分析支持** - 帮助静态代码分析工具按照真实编译选项分析代码
>   4. **辅助调试和导航** - 使代码导航、符号查找等功能更精确
>
>   文件中记录了编译命令、包含路径、宏定义、优化选项等编译器参数，对于像 OpenHarmony 这样的大型项目尤其重要，能让开发工具更精确地分析代码上下文和依赖关系。

它一般长这个样子

```json
 {
    "directory": "/home/xxx/workspace/OpenHarmony-v3.1-Release/out/hispark_pegasus/wifiiot_hispark_pegasus",
    "command": "ccache riscv32-unknown-elf-gcc -D_XOPEN_SOURCE=700 -DOHOS_DEBUG -D__LITEOS__ -D__LITEOS_M__ -I../../../applications/sample/wifi-iot/app/loc_info_collector/gpsM_uart -I../../../applications/sample/wifi-iot/app/loc_info_collector/tools -I../../../applications/sample/wifi-iot/app/loc_info_collector/AT_uart -I../../../applications/sample/wifi-iot/app/loc_info_collector/config -I../../../applications/sample/wifi-iot/app/ssd1306 -I../../../applications/sample/wifi-iot/app/loc_info_collector/OLED_FUN -I../../../applications/sample/wifi-iot/app/loc_info_collector/sys -I../../../applications/sample/wifi-iot/app/loc_info_collector/mqtt -I../../../applications/sample/wifi-iot/app/loc_info_collector/uart -I../../../utils/native/lite/include -I../../../kernel/liteos_m/components/cmsis/2.0 -I../../../base/iot_hardware/interfaces/kits/wifiiot_lite -I../../../base/iot_hardware/peripheral/interfaces/kits -I../../../vendor/hisi/hi3861/hi3861/third_party/lwip_sack/include -I../../../foundation/communication/interfaces/kits/wifi_lite/wifiservice -I../../../device/soc/hisilicon/hi3861v100/hi3861_adapter/hals/communication/wifi_lite/wifiservice -I../../../device/soc/hisilicon/hi3861v100/hi3861_adapter/kal -I../../../third_party/nmealib -I../../../third_party/cJSON -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/include -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/include -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/system/include -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/config -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/config/nv -I../../../utils/native/lite/include -I../../../device/soc/hisilicon/hi3861v100/hi3861_adapter/kal/cmsis -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/os/Huawei_LiteOS/kernel/base/include -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/os/Huawei_LiteOS/targets/hi3861v100/include -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/os/Huawei_LiteOS/kernel/include -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/os/Huawei_LiteOS/arch/risc-v/rv32im -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/os/Huawei_LiteOS/components/lib/libm/include -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/os/Huawei_LiteOS/components/lib/libsec/include -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/os/Huawei_LiteOS/net/wpa_supplicant-2.7/src/common -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/os/Huawei_LiteOS/targets/hi3861v100/plat/riscv -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/os/Huawei_LiteOS/kernel/include -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/os/Huawei_LiteOS/kernel/extended/runstop -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/os/Huawei_LiteOS/components/posix/include -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/os/Huawei_LiteOS/components/linux/include -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/third_party/lwip_sack/include -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/os/Huawei_LiteOS/components/lib/libc/musl/include -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/os/Huawei_LiteOS/components/lib/libc/musl/arch/generic -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/os/Huawei_LiteOS/components/lib/libc/musl/arch/riscv32 -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/os/Huawei_LiteOS/components/lib/libc/hw/include -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/os/Huawei_LiteOS/components/lib/libc/nuttx/include -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/os/Huawei_LiteOS/components/lib/libsec/include -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/os/Huawei_LiteOS/targets/hi3861v100/config -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/os/Huawei_LiteOS/targets/hi3861v100/user -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/os/Huawei_LiteOS/targets/hi3861v100/plat -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/os/Huawei_LiteOS/targets/hi3861v100/extend/include -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/os/Huawei_LiteOS/arch -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/os/Huawei_LiteOS/components/lib/libc/bionic/libm -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/os/Huawei_LiteOS/shell/include -I../../../device/soc/hisilicon/hi3861v100/sdk_liteos/platform/os/Huawei_LiteOS/net/telnet/include -I../../../third_party/cJSON -Os -mabi=ilp32 -falign-functions=2 -msave-restore -fno-optimize-strlen -freorder-blocks-algorithm=simple -fno-schedule-insns -fno-inline-small-functions -fno-inline-functions-called-once -mtune=size -mno-small-data-limit=0 -fno-aggressive-loop-optimizations -std=c99 -Wpointer-arith -Wstrict-prototypes -ffunction-sections -fdata-sections -fno-exceptions -fno-short-enums -Wextra -Wundef -U PRODUCT_CFG_BUILD_TIME -DLOS_COMPILE_LDM -DPRODUCT_USR_SOFT_VER_STR=None -DCYGPKG_POSIX_SIGNALS -D__ECOS__ -D__RTOS_ -DPRODUCT_CFG_HAVE_FEATURE_SYS_ERR_INFO -D__LITEOS__ -DLIB_CONFIGURABLE -DLOSCFG_SHELL -DLOSCFG_CACHE_STATICS -DCUSTOM_AT_COMMAND -DLOS_COMPILE_LDM -DLOS_CONFIG_IPERF3 -DCMSIS_OS_VER=2 -DSECUREC_ENABLE_SCANF_FILE=0 -DCONFIG_AT_COMMAND -DPRODUCT_CFG_CHIP_VER_STR=Hi3861V100 -DCHIP_VER_Hi3861 -DPRODUCT_CFG_SOFT_VER_STR=Hi3861 -DHI_BOARD_ASIC -DHI_ON_FLASH -DLITEOS_WIFI_IOT_VERSION -mabi=ilp32 -falign-functions=2 -msave-restore -fno-optimize-strlen -freorder-blocks-algorithm=simple -fno-schedule-insns -fno-inline-small-functions -fno-inline-functions-called-once -mtune=size -mno-small-data-limit=0 -fno-aggressive-loop-optimizations -std=c99 -Wpointer-arith -Wstrict-prototypes -ffunction-sections -fdata-sections -fno-exceptions -fno-short-enums -Wextra -Wundef -U PRODUCT_CFG_BUILD_TIME -DLOS_COMPILE_LDM -DPRODUCT_USR_SOFT_VER_STR=None -DCYGPKG_POSIX_SIGNALS -D__ECOS__ -D__RTOS_ -DPRODUCT_CFG_HAVE_FEATURE_SYS_ERR_INFO -D__LITEOS__ -DLIB_CONFIGURABLE -DLOSCFG_SHELL -DLOSCFG_CACHE_STATICS -DCUSTOM_AT_COMMAND -DLOS_COMPILE_LDM -DLOS_CONFIG_IPERF3 -DCMSIS_OS_VER=2 -DSECUREC_ENABLE_SCANF_FILE=0 -DCONFIG_AT_COMMAND -DPRODUCT_CFG_CHIP_VER_STR=Hi3861V100 -DCHIP_VER_Hi3861 -DPRODUCT_CFG_SOFT_VER_STR=Hi3861 -DHI_BOARD_ASIC -DHI_ON_FLASH -DLITEOS_WIFI_IOT_VERSION -march=rv32imac -fno-common -fno-builtin -fno-strict-aliasing -Wall -fsigned-char -fstack-protector-all -std=c99 -c ../../../applications/sample/wifi-iot/app/loc_info_collector/mqtt/wb_ram.c -o obj/applications/sample/wifi-iot/app/loc_info_collector/mqtt/libmain_process.wb_ram.o",
    "file": "../../../applications/sample/wifi-iot/app/loc_info_collector/mqtt/wb_ram.c",
    "output": "obj/applications/sample/wifi-iot/app/loc_info_collector/mqtt/libmain_process.wb_ram.o"
  }
```

通过以下的步骤可以生成这个文件

1.   进入build.ninja所在目录: cd out/hispark_pegasus/wifiiot_hispark_pegasus/ 

![image-20250321203936108](https://cdn.jsdelivr.net/gh/kashima19960/img@master/openharmony/image-20250321203936108.png)

1.   compile_commands.json生成指令: ninja -C ./ -t compdb cxx cc > compile_commands.json

这里你其实也发现了，就是将 ninja -C ./ -t compdb cxx cc 的输出重定向到 compile_commands.json 这个文件，所以它不叫compile_commands.json也行，只不过是约定俗成的东西。

1.   将compile_commands.json移动到源码根目录下:mv ./compile_commands.json ../../..

你用 Vscode 移动也行，没必要非得用命令行

4.   看看clangd:idle有没有在转，有在转说明clangd就在索引工程源码了，没有的话，就重启一下 vscode

![image-20250321205850440](https://cdn.jsdelivr.net/gh/kashima19960/img@master/openharmony/image-20250321205850440.png)

## 写成脚本

在你更改Openharmony代码结构的时候，这个 compile_commands.json 要重新生成，不然索引不了你自己最新写的代码文件，但是每次都要进行以上的步骤生成这个文件很麻烦，所以我一般都把它写成一个bash脚本

```bash
#!/bin/bash

# 把这个workspace的路径改成你自己的工程源码路径，其他的不用动
workspace=~/workspace/OpenHarmony-v3.1-Release/

cd $workspace/out/hispark_pegasus/wifiiot_hispark_pegasus/

# 生成 compile_commands.json
ninja -C $workspace/out/hispark_pegasus/wifiiot_hispark_pegasus/ -t compdb cxx cc > compile_commands.json

# 将 compile_commands.json 移动到源码根目录下
mv compile_commands.json $workspace
```

## 有个问题

用这个方法，Vscode会提示有些参数无法识别

临时的解决方法就是把这些参数删除

```bash
#!/bin/bash

# 进入 build.ninja 所在目录
workspace=~/workspace/OpenHarmony-v3.1-Release/

cd $workspace/out/hispark_pegasus/wifiiot_hispark_pegasus/

# 生成 compile_commands.json
ninja -C $workspace/out/hispark_pegasus/wifiiot_hispark_pegasus/ -t compdb cxx cc > compile_commands.json

# 使用sed删除不需要的参数
sed -i 's/-fno-optimize-strlen//g' compile_commands.json
sed -i 's/-freorder-blocks-algorithm=simple//g' compile_commands.json
sed -i 's/-mno-small-data-limit=0//g' compile_commands.json
sed -i 's/-fno-aggressive-loop-optimizations//g' compile_commands.json

# 清理可能产生的多余空格（参数之间可能有多个空格）
sed -i 's/  / /g' compile_commands.json

# 将 compile_commands.json 移动到源码根目录下
mv compile_commands.json $workspace

```



![image-20250321210936632](https://cdn.jsdelivr.net/gh/kashima19960/img@master/openharmony/image-20250321210936632.png)

虽然不影响智能提示，但是我也不知道为什么这些参数会报错，如果有大神知道怎么解决，可以给我发个邮箱CodingCV@outlook.com 或者在评论区留言教一下我啊😊😊

