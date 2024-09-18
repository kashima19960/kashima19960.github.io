---
title: 一键更换软件源的工具——chsrc
date: 2024-09-17 16:53:40
tags: 其他
---
## 前言

经常用pip，ubuntu的apt，或者centos的yum等包下载工具的人不可避免的一件事就是——“更换软件源”，因为以上三个包下载工具的软件源一般都是默认为国外的官方网站，由于国情问题，下载速度就会非常慢，所以我们使用这些包下载工具通常都会换源，但是更换软件源是一个比较麻烦的步骤，而且每个不同的包下载器的配置方法都是异构的，通常我可以用以下的步骤概括一下：

1. 上网搜索相关的教程，找到想要更换的对应包下载工具软件源的方法
2. 找到下载速度比较快，而且稳定的镜像站
3. 找到包下载工具的配置文件，进行更改

而且不同的包下载工具，上面的步骤都是不一样的，所以就存在以下的痛点了：

1. 不同镜像站的下载速度你要自己测量，很麻烦
2. 不同包下载工具的配置文件的存放位置与修改方法都是异构的
3. 在网上找教程经常会遇到互联网垃圾，需要一个个过滤

于是！🤓我就找到了一个很好用的换源工具——[chsrc](https://github.com/RubyMetric/chsrc),这个命令行工具完美解决了以上的痛点，并且支持绝大多数的包下载器与系统换源(下面展示)

## 效果图

还是老规矩，好不好用，直接看图说话，说再多都是虚的😊。

### 可用对象

可用镜像站和可换源目标有很多，不过对我来说比较常用的就几个，pip ,ubuntu，npm，conda,anaconda

```bash
D:\kashima19960.github.io>chsrc list
指定使用某源，请使用 chsrc set <target> <code>
可用镜像站: 

  code         镜像站简写                  镜像站URL                              镜像站
---------    --------------    -------------------------------------     ---------------------
mirrorz       MirrorZ           https://mirrors.cernet.edu.cn/            MirrorZ 校园网镜像站
tuna          TUNA              https://mirrors.tuna.tsinghua.edu.cn/     清华大学开源软件镜像站
sjtu          SJTUG-zhiyuan     https://mirrors.sjtug.sjtu.edu.cn/        上海交通大学致远镜像站
zju           ZJU               https://mirrors.zju.edu.cn/               浙江大学开源软件镜像站
lzu           LZUOSS            https://mirror.lzu.edu.cn/                兰州大学开源社区镜像站
jlu           JLU               https://mirrors.jlu.edu.cn/               吉林大学开源镜像站
bfsu          BFSU              https://mirrors.bfsu.edu.cn/              北京外国语大学开源软件镜像站
pku           PKU               https://mirrors.pku.edu.cn/               北京大学开源镜像站
bjtu          BJTU              https://mirror.bjtu.edu.cn/               北京交通大学自由与开源软件镜像站
sustech       SUSTech           https://mirrors.sustech.edu.cn/           南方科技大学开源软件镜像站
ustc          USTC              https://mirrors.ustc.edu.cn/              中国科学技术大学开源镜像站
hust          HUST              https://mirrors.hust.edu.cn/              华中科技大学开源镜像站
nju           NJU               https://mirrors.nju.edu.cn/               南京大学开源镜像站
ali           Ali OPSX          https://developer.aliyun.com/mirror/      阿里巴巴开源镜像站
tencent       Tencent           https://mirrors.tencent.com/              腾讯软件源
huawei        Huawei Cloud      https://mirrors.huaweicloud.com/          华为开源镜像站
volc          Volcengine        https://developer.volcengine.com/mirror/  火山引擎开源软件镜像站
netease       Netease           https://mirrors.163.com/                  网易开源镜像站
sohu          SOHU              https://mirrors.sohu.com/                 搜狐开源镜像站
api7          api7.ai           https://www.apiseven.com/                 深圳支流科技有限公司
fit2cloud     FIT2CLOUD         https://www.fit2cloud.com/                杭州飞致云信息科技有限公司
rubychina     RubyChina         https://gems.ruby-china.com/              Ruby China 社区
emacschina    EmacsChina        https://elpamirror.emacs-china.org/       Emacs China 社区
npmmirror     npmmirror         https://npmmirror.com/                    npmmirror (阿里云赞助)
goproxy.cn    Goproxy.cn        https://goproxy.cn/                       Goproxy.cn (七牛云)
goproxy.io    GOPROXY.IO        https://goproxy.io/                       GOPROXY.IO

支持对以下目标换源 (同一行表示这几个命令兼容)

编程语言
-------------------------
gem     ruby    rubygem rb      rubygems        bundler
pip     python  pypi    py      poetry  pdm
npm     node    nodejs  js      yarn    pnpm
perl    cpan
php     composer
lua     luarocks
rust    cargo   crate   crates
go      golang  goproxy
java    maven   mvn     gradle
clojure clojars cloj    lein    leiningen
dart    pub     flutter
haskell cabal   stack   hackage
ocaml   opam
cran    r
julia

操作系统
-------------------------
debian
ubuntu
linuxmint       mint
kali
trisquel
lite    linuxlite
raspi   raspberrypi
armbian
openwrt opkg    LEDE
deepin
openkylin
ros     ros2
fedora
rocky   rockylinux
alma    almalinux
openeuler
openanolis      anolis
opensuse
arch    archlinux
archlinuxcn     archcn
manjaro
gentoo
alpine
void    voidlinux
solus
msys2   msys
freebsd
netbsd
openbsd

软件
-------------------------
winget
brew    homebrew
cocoa   cocoapods       pod     cocoapod
dockerhub       docker
flathub flatpak
nix
guix
emacs   elpa
latex   ctan    tex     texlive miktex  tlmgr   mpm
conda   anaconda
```

### 测速功能

`chsrc`能一键帮你测试所有镜像站的连接速度，并且给出最高值

![image-20240917172228941](https://raw.githubusercontent.com/kashima19960/img/master/%E4%B8%80%E9%94%AE%E6%9B%B4%E6%8D%A2%E8%BD%AF%E4%BB%B6%E6%BA%90%E7%9A%84%E5%B7%A5%E5%85%B7%E2%80%94%E2%80%94chsrc%20/image-20240917172228941.png)

### 一键换源

`chsrc`能在测量镜像站速度后，自己替你更换速度最快的源

![image-20240917172540336](https://raw.githubusercontent.com/kashima19960/img/master/%E4%B8%80%E9%94%AE%E6%9B%B4%E6%8D%A2%E8%BD%AF%E4%BB%B6%E6%BA%90%E7%9A%84%E5%B7%A5%E5%85%B7%E2%80%94%E2%80%94chsrc%20/image-20240917172540336.png)

## 安装与使用

### 安装

作者都打包到了一个exe文件(windows系统)或者一个shell脚本中(linux系统)，因此下载后就能立刻使用了，不需要安装，根据自己的系统下载对应的版本即可[Release v0.1.8 · RubyMetric/chsrc (github.com)](https://github.com/RubyMetric/chsrc/releases/tag/v0.1.8)，如果你访问不了github,那就通过国内的gitee下载[v0.1.8 · RubyMetric/chsrc - Gitee.com](https://gitee.com/RubyMetric/chsrc/releases/tag/v0.1.8)。**下面我介绍一种从来没接触过命令行的萌新的安装方法**，大佬的话，建议直接看[官方文档](https://github.com/RubyMetric/chsrc)

`chsrc`是一个命令行工具，想要使用必须在命令行中调用，但是下载完后，直接在命令行敲 `chsrc`是没有用的,因为shell无法搜索到这个路径(这个解释起来会是长篇大论，因此这里跳过)

![image-20240917174408602](https://raw.githubusercontent.com/kashima19960/img/master/%E4%B8%80%E9%94%AE%E6%9B%B4%E6%8D%A2%E8%BD%AF%E4%BB%B6%E6%BA%90%E7%9A%84%E5%B7%A5%E5%85%B7%E2%80%94%E2%80%94chsrc%20/image-20240917174408602.png)

有两种方法，能让你调用到这个工具

1. 进入到这个工具所在的根目录，比如我把工具下载到了D:\temp下

![image-20240917174531031](https://raw.githubusercontent.com/kashima19960/img/master/%E4%B8%80%E9%94%AE%E6%9B%B4%E6%8D%A2%E8%BD%AF%E4%BB%B6%E6%BA%90%E7%9A%84%E5%B7%A5%E5%85%B7%E2%80%94%E2%80%94chsrc%20/image-20240917174531031.png)

在命令行界面，我们 `cd`进去更改目录到工具的根目录

![image-20240917174621243](https://raw.githubusercontent.com/kashima19960/img/master/%E4%B8%80%E9%94%AE%E6%9B%B4%E6%8D%A2%E8%BD%AF%E4%BB%B6%E6%BA%90%E7%9A%84%E5%B7%A5%E5%85%B7%E2%80%94%E2%80%94chsrc%20/image-20240917174621243.png)

然后执行

```bash
.\chsrc-x64-windows.exe
```

这个 `.\`是不能省略的，表示当前目录的意思，如果是Linux系统的话，要用斜杠 `./`

![image-20240917174805429](https://raw.githubusercontent.com/kashima19960/img/master/%E4%B8%80%E9%94%AE%E6%9B%B4%E6%8D%A2%E8%BD%AF%E4%BB%B6%E6%BA%90%E7%9A%84%E5%B7%A5%E5%85%B7%E2%80%94%E2%80%94chsrc%20/image-20240917174805429.png)

2. 添加环境变量

把 `D:\temp`(这里改成你的chsrc的安装位置)，添加到环境变量中，这样就不需要在工具所在目录使用了，其他系统怎么添加环境变量，自行百度

![image-20240917175106282](https://raw.githubusercontent.com/kashima19960/img/master/%E4%B8%80%E9%94%AE%E6%9B%B4%E6%8D%A2%E8%BD%AF%E4%BB%B6%E6%BA%90%E7%9A%84%E5%B7%A5%E5%85%B7%E2%80%94%E2%80%94chsrc%20/image-20240917175106282.png)

![image-20240917175228447](https://raw.githubusercontent.com/kashima19960/img/master/%E4%B8%80%E9%94%AE%E6%9B%B4%E6%8D%A2%E8%BD%AF%E4%BB%B6%E6%BA%90%E7%9A%84%E5%B7%A5%E5%85%B7%E2%80%94%E2%80%94chsrc%20/image-20240917175228447.png)

说起来，这个 `chsrc-x64-windows.exe`名字太长了，你可以直接改个名字叫 `chsrc.exe`

![image-20240917175416490](https://raw.githubusercontent.com/kashima19960/img/master/%E4%B8%80%E9%94%AE%E6%9B%B4%E6%8D%A2%E8%BD%AF%E4%BB%B6%E6%BA%90%E7%9A%84%E5%B7%A5%E5%85%B7%E2%80%94%E2%80%94chsrc%20/image-20240917175416490.png)

这样在命令行就不用敲那么长的名字了

![image-20240917175507271](https://raw.githubusercontent.com/kashima19960/img/master/%E4%B8%80%E9%94%AE%E6%9B%B4%E6%8D%A2%E8%BD%AF%E4%BB%B6%E6%BA%90%E7%9A%84%E5%B7%A5%E5%85%B7%E2%80%94%E2%80%94chsrc%20/image-20240917175507271.png)

### 使用

`chsrc`有以下的使用方法，看似很多，其实常用的就两三个

```bash
D:\kashima19960.github.io>chsrc
chsrc: Change Source (GPLv3+) v0.1.8-2024/08/23 by RubyMetric

使用: chsrc <command> [options] [target] [mirror]
help                      打印此帮助，或 h, -h, --help
issue                     查看相关issue

list (或 ls, 或 l)        列出可用镜像源，和可换源目标
list mirror/target        列出可用镜像源，或可换源目标
list os/lang/ware         列出可换源的操作系统/编程语言/软件

measure <target>          对该目标所有源测速
cesu    <target>

list <target>             查看该目标可用源与支持功能
get  <target>             查看该目标当前源的使用情况

set  <target>             换源，自动测速后挑选最快源
set  <target>  first      换源，使用维护团队测速第一的源
set  <target> <mirror>    换源，指定使用某镜像站 (通过list <target>查看)
set  <target> https://url 换源，用户自定义源URL
reset <target>            重置，使用上游默认使用的源

选项:
-dry                      Dry Run，模拟换源过程，命令仅打印并不运行
-ipv6                     使用IPv6测速
-local                    仅对本项目而非全局换源 (通过ls <target>查看支持情况)
-en(glish)                使用英文输出
-no-color                 无颜色输出

维护: <https://github.com/RubyMetric/chsrc>
```

1. `chsrc list`,列出所有可用源，效果图中已经演示过
2. ` chsrc set <target> <code>`,这个target指的是 `chsrc list`列出的目标，比如pip,ubuntu，conda之类的，这个code一般指镜像站的url或者代号，不指定的话，就会测量出速度最快的镜像站，然后设置成该镜像站的软件源

![image-20240917184108029](https://raw.githubusercontent.com/kashima19960/img/master/%E4%B8%80%E9%94%AE%E6%9B%B4%E6%8D%A2%E8%BD%AF%E4%BB%B6%E6%BA%90%E7%9A%84%E5%B7%A5%E5%85%B7%E2%80%94%E2%80%94chsrc%20/image-20240917184108029.png)

3. `chsrc reset <target> <code>`,用法跟 `chsrc set`类似,用来重置软件源，比如重置pip为官方的软件源

![image-20240917184441577](https://raw.githubusercontent.com/kashima19960/img/master/%E4%B8%80%E9%94%AE%E6%9B%B4%E6%8D%A2%E8%BD%AF%E4%BB%B6%E6%BA%90%E7%9A%84%E5%B7%A5%E5%85%B7%E2%80%94%E2%80%94chsrc%20/image-20240917184441577.png)

## 结语

本文旨在分享好用的开源软件，如果你觉得这个换源工具很好用，请多多支持原作者和这个开源项目！！
