---
title: 屏蔽csdn搜索结果的方法
date: 2024-08-08 22:20:00
tags: 其他
---
## 前言

鉴于你对知识质量的渴望，以及对挖掘知识金子的欲求，你一定想在浏览器结果中去除有关Csdn的全部内容😈**(确信)**，但是当你在用bing或者google搜索有没有可以屏蔽CSDN搜索结果的方法时，通常会有以下的结果，这些方法我基本上都尝试过，而且没啥用处，因此下面我分享一个确实有用的方法给大家。

![image-20240808214659656](https://raw.githubusercontent.com/kashima19960/img/master/%E5%B1%8F%E8%94%BDcsdn%20/image-20240808214659656.png)

## 效果图

老规矩，我喜欢在看一系列繁琐的步骤前先看看效果，这样我才有继续看下去的欲望，相信大多数人都是这样想的😝

![image-20240808215045912](https://raw.githubusercontent.com/kashima19960/img/master/%E5%B1%8F%E8%94%BDcsdn%20/image-20240808215045912.png)

假设你非是不信邪，尝试通过在地址栏直接通过csdn的官网进行访问，会得到下面的结果

![image-20240808215248191](https://raw.githubusercontent.com/kashima19960/img/master/%E5%B1%8F%E8%94%BDcsdn%20/image-20240808215248191.png)

## 步骤

1.   至少拥有一个脚本管理器，比如[tampermonkey](https://microsoftedge.microsoft.com/addons/detail/篡改猴/iikmkjmpaadaobahmlepeloendndfphd),安装后可以在浏览器的扩展选项卡中查看是否安装成功

<img src="https://raw.githubusercontent.com/kashima19960/img/master/%E5%B1%8F%E8%94%BDcsdn%20/image-20240808215820344.png" alt="image-20240808215820344" style="zoom:50%;" />

2.   下载屏蔽脚本[Fuck CSDN (greasyfork.org)](https://greasyfork.org/zh-CN/scripts/441726-csdn)
3.   打开tampermonkey,如何有相应的图标说明就安装成功了
   ![image-20240808220357016](https://raw.githubusercontent.com/kashima19960/img/master/%E5%B1%8F%E8%94%BDcsdn%20/image-20240808220357016.png)
4.   尝试在搜索栏搜索相关内容，就能发现脚本将所有csdn相关的内容都隐去了

>   注：这个脚本只支持 Google / Baidu / Bing / 360 搜索，对于一些不常用的搜索引擎是没用的

## 脚本原理分析(可以不看)

这个部分，我来分析一下这个脚本实现的原理，虽然说是不必要的，但是学习一下原作者的代码思维还是有用的

```js
// 检测当前页面是否属于特定的域名
function isSite(domain) {
    return window.location.href.match(new RegExp("^https?:\/\/[\\w.]+?" + domain))
}

// 隐藏CSDN内容的函数
function HideCSDN(){
    // 定义一组CSS选择器，用于匹配可能包含CSDN链接的元素
    const filters = ".source_1Vdff, .iUh30, .b_attribution, .g-linkinfo-a".split(", ")
    // 选择所有可能的搜索结果元素
    const Elements=document.querySelectorAll(".result.c-container, .g, .b_algo, .res-list");
    let num; // 用于记录移除的CSDN链接数量
    // 遍历所有搜索结果元素
    Elements.forEach(function(Item,i){
        // 遍历CSS选择器
        for (var filter in filters) {
            // 查找匹配选择器的子元素
            let selectedContent=Item.querySelector(filters[filter])
            // 如果找到包含"CSDN"文本的元素，则移除整个搜索结果项
            if (selectedContent !== null) {
                if (selectedContent.innerText.toLowerCase().includes("csdn")) {
                    Item.parentNode.removeChild(Item);
                    num = i; // 记录移除的元素索引
                    break;
                }
            }
        }
    });
    // 如果有移除的链接，则在控制台输出移除信息
    if (num !== undefined) {
        console.log(`[Fuck CSDN] 已去除 ${num} 条 CSDN 内容`)
    }
}

// 绑定事件监听器的函数
function bind() {
    // 为翻页按钮等元素添加事件监听器
    document.querySelectorAll(".page-item_M4MDr, #form, #page, .ac_wrap").forEach(
        function(Item) {
            // 当用户与这些元素交互时，延迟执行HideCSDN函数
            Item.addEventListener('mousedown',function () {
                setTimeout(function(){
                    HideCSDN();
                    // 对于360搜索，重新绑定事件监听器
                    if (isSite('so.com')) {
                        bind();
                    }
                },1000);
            })
        }
)}

// 为搜索框添加回车键事件监听器
document.querySelectorAll("input.gLFyf.gsfi, input#kw, input#keyword").forEach(
function(Item) {
    // 当用户按下回车键进行搜索时，延迟执行HideCSDN函数
    Item.addEventListener('keydown', function () {
    var evt = window.event || arguments.callee.caller.arguments[0];
    if (evt.keyCode == "13") {
        setTimeout(function(){HideCSDN();},1000);
    }
})})

// 如果用户直接访问CSDN，则阻止访问并后退
if (isSite('csdn.net')) {
    document.body.innerHTML = "Blocked by Fuck CSDN.";
    window.history.go(-1);
}

// 初始执行隐藏CSDN内容的函数
HideCSDN();
// 绑定事件监听器
bind();

```