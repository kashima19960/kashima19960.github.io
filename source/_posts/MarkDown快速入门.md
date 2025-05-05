---
title: Markdown快速入门
date: 2025-03-26 10:50:00
tags: 其他
---
## 前言

我平时写作用的最多的就是markdown，甚至比word文档还频繁，所以这篇文章我简单记录一下markdown常用语法

## markdown有啥用？

我在学习任何东西之前，都会思考一下学这个东西有啥用，因为时间是很宝贵的，我们只能将自己人生中有限的时间来做有限的事情，所以我说说自己对markdown的看法

### 优点

1. 适合做笔记

其实我们很多时候做笔记，只是想快速记录一些比较重要的东西，因为markdown其实就是相当于纯文本的基础上加了一些比较常用的写作格式，所以用markdown记录东西是非常快速的

2. 大语言模型优化

现在所有的大语言模型，他都是输出 markdown 格式，不信的话，你可以把大语言模型的输出粘贴到markdown 编辑器中，立刻就能渲染，另一个就是如果你用 markdown 去问Ai问题，会更容易被识别

3. 简单，不用排版

word文档的功能非常强大，但是它的排版非常恶心，想必经常用word文档的同学深有体会，在你改动了某个地方的排版的时候，另一个不知道的地方也莫名其妙发生了格式变动，markdown没有排版，写啥就是啥，简单好用

### 缺点

一个产品不可能都是优点，我这里说一下markdown的劣势

1. 插入图片麻烦

markdown是不能把直接把图片嵌入到内容里面的，只能通过外链的方法进行显示，当然也有用base64转图片这种野路子，但始终不是个好用的方法。图片跟内容分开存，在上传云平台的时候就会非常麻烦

## 常用知识

Markdown的核心理念是"易读易写"，不需要复杂的编辑器，用记事本也能写出漂亮的格式。

### 1. 标题

标题使用 `#`符号来表示，一个 `#`是一级标题，两个 `#`是二级标题，以此类推，最多支持六级标题。记得 `#`后面要空一格😋

```markdown
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题
```

效果如下：

![1742963190487](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/1742963190487.png)

### 2. 强调文本

想要强调某段文字？超简单！

```markdown
*斜体文本* 或 _斜体文本_
**粗体文本** 或 __粗体文本__
***粗斜体文本*** 或 ___粗斜体文本___
```

看看效果：*斜体文本* **粗体文本** ***粗斜体文本***

### 3. 列表

列表分为无序列表和有序列表，使用起来也很简单！

无序列表可以用 `-`、`*`或 `+`作为标记：

```markdown
- 项目一
- 项目二
  - 子项目A
  - 子项目B
```

有序列表则使用**数字**加上一个**小数点**：

```markdown
1. 第一步
2. 第二步
3. 第三步
```

嵌套列表时，子项目前面要缩进两个空格，这样才能形成层级关系😈

### 4. 链接与图片

链接和图片的语法非常相似，只是图片前多了一个感叹号！

```markdown
[链接文字](链接地址 "可选标题")
![图片描述](图片地址 "可选标题")
```

例如：

```markdown
[我的GitHub](https://github.com/kashima19960)
![示例图片](https://cdn.jsdelivr.net/gh/kashima19960/img@master/example.png)
```

### 5. 引用

引用别人的话？用 `>`符号：

```markdown
> 这是一段引用文字
> 这是引用的第二行
> 
> > 这是嵌套引用
```

效果如下：

![1742963319245](https://cdn.jsdelivr.net/gh/kashima19960/img@master/%E5%85%B6%E4%BB%96/1742963319245.png)

### 6. 代码

行内代码用反引号(键盘TAB上面哪个键)包裹：`console.log('Hello World')`

代码块则使用三个反引号，并可以指定语言类型：

```javascript
function sayHello() {
  console.log('Hello, Markdown!');
}
```

### 7. 表格

表格看起来复杂，其实很简单：

```markdown
| 表头1 | 表头2 | 表头3 |
| ----- | :---: | ----: |
| 左对齐 | 居中 | 右对齐 |
| 内容 | 内容 | 内容 |
```

`:---`表示左对齐，`:---:`表示居中，`---:`表示右对齐。

### 8. 分割线

三个或更多的 `-`、`*`或 `_`都可以创建分割线：

```markdown
---
***
___
```

## 实战演练

让我们用学到的知识写一个简单的笔记：

```markdown
# 我的项目计划

## 目标

建立一个**个人博客网站**，分享技术文章和个人感悟。

## 任务列表

1. 学习Markdown基础
   - [x] 掌握基本语法
   - [ ] 尝试高级功能
2. 选择博客平台
   - [ ] 研究GitHub Pages
   - [ ] 考虑Hexo框架

> 记住：坚持每周至少更新一篇文章！

---

### 参考资料
[Markdown官方文档](https://daringfireball.net/projects/markdown/)
```

## 结语

markdown常用的就以上这些了，当然markdown想玩出花来也是可以的，比如嵌入html和css实现各种花里胡哨的效果，或者是插入mermaid代码生成流程图，但是这些等你要用到再去了解这些高级用法也不迟，先把基础学好才是最重要的

## 参考资料

学习Markdown，以下资源可能对你有所帮助：

1. [Markdown 官方网站](https://daringfireball.net/projects/markdown/) - John Gruber 创建的原始 Markdown 规范
2. [GitHub Flavored Markdown](https://github.github.com/gfm/) - GitHub 使用的 Markdown 扩展语法
3. [Markdown 指南](https://www.markdownguide.org/) - 全面且易懂的 Markdown 学习资源
4. [CommonMark](https://commonmark.org/) - 标准化的 Markdown 规范
5. [Typora](https://typora.io/) - 所见即所得的 Markdown 编辑器
6. [VS Code Markdown 扩展](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) - VS Code 中增强 Markdown 体验的扩展
7. [Mermaid 流程图语法](https://mermaid-js.github.io/mermaid/#/) - 用于在 Markdown 中创建图表和流程图

这些资源涵盖了从基础到高级的各个方面，当你想深入学习 Markdown 时可以参考。
