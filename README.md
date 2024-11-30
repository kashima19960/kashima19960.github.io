# 个人博客

## 项目简介

这是一个基于Hexo框架的个人博客项目，使用了Butterfly主题。项目主要用于记录学习历程和个人随笔。

## 依赖项版本要求

为了确保项目的顺利运行，请确保使用以下版本的依赖项：

- Hexo: 7.3.0
- Hexo主题: Butterfly
- nodejs-lts : 22.11.0 
- npm: 10.9.0

## 安装与运行

### 1. 安装依赖

在项目根目录下运行以下命令来安装所需的依赖：

```bash
npm install
```

### 2. 配置主题

在项目根目录下找到`_config.yml`文件，将主题配置为`Butterfly`：

```yaml
theme: butterfly
```

### 3. 启动服务器

使用以下命令启动Hexo服务器：

```bash
hexo server
```

启动后，打开浏览器访问`http://localhost:4000`，即可查看运行中的项目。

## 部署

### 1. 生成静态文件

使用以下命令生成静态文件：

```bash
hexo generate
```

### 2. 部署到GitHub Pages

在`_config.yml`文件中，确保已经配置了部署选项：

```yaml
deploy:
  type: git
  repo: git@github.com:kashima19960/kashima19960.github.io.git
```

然后运行以下命令进行部署：

```bash
hexo deploy
```

部署完成后，您可以通过配置的GitHub Pages地址访问您的项目，例如：`https://kashima19960.github.io/`

## 参考文档

- [Hexo官方文档](https://hexo.io/docs/)
- [Butterfly主题文档](https://butterfly.js.org/)
