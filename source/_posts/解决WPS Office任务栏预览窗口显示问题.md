---
title: 解决WPS Office任务栏预览窗口会显示多个窗口的问题
date: 2025-06-16 10:30:00
tags: 其他
---
## 前言

在使用WPS Office的时候，经常会遇到一个令人头疼的问题——任务栏预览窗口显示😩。有时候你打开了多个WPS文档，由于WPS是多标签页的，所以在任务栏预览窗口预期应该只有一个，但是WPS默认是会显示多个窗口

## 问题现象

![1750040208337](https://cdn.jsdelivr.net/gh/kashima19960/img@master/stm32/1750040208337.png)

## 解决方法

 修改注册表，将下面的内容保存为 `DisableMultiTaskbar_ForAll.reg`，然后双击执行。或者从官方提供的链接下载 [DisableMultiTaskbar 工具](https://kdocs.cn/l/ckXxc3GUddhf)

```bash
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\kingsoft\Office\6.0\wpsoffice\Application Settings]
"enable_multi_taskbar"=dword:00000000

[HKEY_CURRENT_USER\Software\kingsoft\Office\6.0\et\Application Settings]
"enable_multi_taskbar"=dword:00000000

[HKEY_CURRENT_USER\Software\kingsoft\Office\6.0\wps\Application Settings]
"enable_multi_taskbar"=dword:00000000

[HKEY_CURRENT_USER\Software\kingsoft\Office\6.0\wpp\Application Settings]
"enable_multi_taskbar"=dword:00000000

[HKEY_CURRENT_USER\Software\kingsoft\Office\6.0\pdf\Application Settings]
"enable_multi_taskbar"=dword:00000000

```


想改回来也行 将下面的内容保存为 `EnableMultiTaskbar_ForAll.reg`，然后双击执行。或者从官方提供的链接下载 [EnableMultiTaskbar 工具](https://kdocs.cn/l/chhE2yMlZ0o3)

```bash

Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\kingsoft\Office\6.0\wpsoffice\Application Settings]
"enable_multi_taskbar"=dword:00000001

[HKEY_CURRENT_USER\Software\kingsoft\Office\6.0\et\Application Settings]
"enable_multi_taskbar"=dword:00000001

[HKEY_CURRENT_USER\Software\kingsoft\Office\6.0\wps\Application Settings]
"enable_multi_taskbar"=dword:00000001

[HKEY_CURRENT_USER\Software\kingsoft\Office\6.0\wpp\Application Settings]
"enable_multi_taskbar"=dword:00000001

[HKEY_CURRENT_USER\Software\kingsoft\Office\6.0\pdf\Application Settings]
"enable_multi_taskbar"=dword:00000001

```

做出修改后，要重启 WPS 才能生效
