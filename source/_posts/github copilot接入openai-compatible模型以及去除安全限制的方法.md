---
title: github copilot接入openai-compatible模型以及去除安全限制的方法
date: 2025-07-28 19:19:40
tags: 其他
---
## 重要说明

本文具有时效性，请注意检查信息的正确性！

## 前言

copilot只支持那几家国外的模型提供商，除了openrouter以外我们都很难进行访问和支付，以及copilot系统提示词会拒绝回答非编程的问题，这点也让我很苦恼
所以为了完成我的这两个需求

1. github copilot chat能接入自定义的openai-compatible模型
2. 删除saferule(安全规则)

我去查找了相关的开源社区寻找解决方法，由于copilot chat前些日子开源了，所以这个第一个功能有开发者做了，但是微软还没有发布release版本，所以我们需要手动打包扩展，第二个功能可以通过修改系统提示词来实现。

## 具体步骤

1. 先把仓库克隆下来，这里要注意，这个开发者把功能commit到了feat-ui分支，不要下载到了main分支

```bash
git clone -b  feat-ui https://github.com/relic-yuexi/vscode-copilot-chat.git
```

2. 删除相关的安全限制(可选)
   找到这个文件 `src\extension\prompts\node\base\safetyRules.tsx`，这个文件是安全规则提示词的底层文件，会被所有代码引用，所以我们只修改这个文件就行,
   如下图可以看到，这下我们知道为什么问非编程问题，会一直回答"Sorry, I can't assist with that."了，把这个字符串替换成任意的词即可

![1753703634313](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/1753703634313.png)

然后再找到这个文件  `src\extension\prompts\node\base\copilotIdentity.tsx` ，这个提示词强制了无论你询问任何模型是谁，都会回答你 "github copilot ",我不喜欢这个，所以把他替换成空格或者其他的提示词

![1753703897738](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/1753703897738.png)

3. 开始构建扩展，并打包成vsix文件

首先确保你已经安装了Node.js和npm，没安装就自己搜索安装一下，不需要啥专业知识的，然后在项目根目录下打开终端，执行以下命令：

安装依赖

```bash
npm install
```

等待完成后，执行：

```bash
npx tsx .esbuild.ts
```

安装打包工具vsce，这个工具用来将项目打包成VSIX格式

```bash
npm install -g vsce
```

最后执行：

```bash
vsce package
```

就这四个命令

1. `npm install` - 安装依赖
2. `npx tsx .esbuild.ts` - 构建项目
3. `npm install -g vsce` - 安装打包工具
4. `vsce package` - 生成VSIX文件

执行完成后，你会在项目根目录看到一个 `.vsix` 文件，这就是可以安装的VS Code扩展包。

**安装扩展：**

- 在VS Code中按 `Ctrl+Shift+P`
- 输入 "Extensions: Install from VSIX"
- 选择生成的 `.vsix` 文件

另一种方法就是打开vscode的插件市场，点击右上角的三个点，最后一个选项就是了

![1753704416207](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/1753704416207.png)



>   2025-7-30更新：评论区有人问怎么添加模型，之前没写，我以为大家都会，下面补充一下

## 添加openai-compatible模型的方法

1.   先打开模型选择器，点击`manage models`

![image-20250730230507853](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/image-20250730230507853.png)

2.   点击红框那一栏，这一栏在你成功按照上述方法构建了扩展后就会有了，官方的copilot目前还没有，你找不到就要检查一下自己有没有安装好扩展了

![image-20250730230558393](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/image-20250730230558393.png)

3.   理论上，只要是能兼容 openai 格式的模型供应商都能添加，这个具体你要看对应的模型供应商，国内基本上知名的模型都是兼容openai格式的，这里我以deepseek为例，由于我这里已经添加过了(看上图就知道了)，这里是取名(名字任意)，然后回车



![image-20250730231149520](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/image-20250730231149520.png)

输入base_url，这里找对应的文档自己查，回车

![image-20250730231256178](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/image-20250730231256178.png)

右下角会提示成功，

![image-20250730231323959](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/image-20250730231323959.png)

再次打开模型选择器就能看到了

![image-20250730231450547](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/image-20250730231450547.png)

点进去，输入apikey，这里你要输入正确的apikey，不然获取model会失败，我这里由于已经添加过deepseek的模型了，所以图片中的 apikey 是我乱填的😋

![image-20250730231610386](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/image-20250730231610386.png)

把模型id输入一下，具体id看对应的官方文档

![image-20250730231843822](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/image-20250730231843822.png)

4.   测试是否添加成功

     由于上述的步骤去除了安全规则和自我介绍，所以可以直接向模型问一些非编程问题，可以看到下图，如果问原版的copilot，他是不会回答你跟模型有关的任何信息的，只会回答“ 我是github copilot”

     

![image-20250730232230150](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/image-20250730232230150.png)

## 已经打包好的扩展

如果你连上述的步骤都没办法完成的话，那就用我打包好的扩展吧，等我有空再弄 😕
