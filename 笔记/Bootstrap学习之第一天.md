# Bootstrap学习之第一天

1.启用Bootstrap

* 下载后使用[《Bootstrap》](https://v3.bootcss.com/getting-started/)
* 使用官方提供的免费CDN加速服务

```html
<!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- 可选的 Bootstrap 主题文件（一般不用引入） -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

<!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
```
2. 基本的HTML模板

```html
<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <title>Bootstrap 101 Template</title>

    <!-- Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- HTML5 shim 和 Respond.js 是为了让 IE8 支持 HTML5 元素和媒体查询（media queries）功能 -->
    <!-- 警告：通过 file:// 协议（就是直接将 html 页面拖拽到浏览器中）访问页面时 Respond.js 不起作用 -->
    <!--[if lt IE 9]>
      <script src="https://cdn.jsdelivr.net/npm/html5shiv@3.7.3/dist/html5shiv.min.js"></script>
      <script src="https://cdn.jsdelivr.net/npm/respond.js@1.4.2/dest/respond.min.js"></script>
    <![endif]-->
</head>

<body>
    <h1>你好，世界！</h1>

    <!-- jQuery (Bootstrap 的所有 JavaScript 插件都依赖 jQuery，所以必须放在前边) -->
    <script src="https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js"></script>
    <!-- 加载 Bootstrap 的所有 JavaScript 插件。你也可以根据需要只加载单个插件。 -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/js/bootstrap.min.js"></script>
</body>

</html>
```

3. 具体的使用方法
* 标题(h1~h6)，同时还定义了(.h1~.h6)六个类名

```html
<h1>标题一</h1>
等同于
<div class="h1">标题一</div>
```

* 副标题<small>标签和.small类（写在<h1>和.h1等标题标签内部）

```html
<h1>主标题<small>副标题</small></h1>
<div class="h1">主标题<small>副标题</small></div>
```
* 段落<p>标签
* 强调内容<small><strong><en><cite>标签和.lead的类

```html
<p><small>这是强调一</small></p>

<p><strong>这是强调二</strong></p>

<P><em>这是强调三</em></p>

<p><cite>这是强调四</cite></p>

<p class="lead">这是强调五</p>
```

* 粗体<b>标签和<strong>标签
* 斜体<em>标签和<i>标签
* 强调有关的类

| 类名          | 颜色           |意义|
| ---------     | --------      |-------|
| .text-muted   | 浅灰色（#999） |提示|
| .text-primary |蓝色(#428bca)   |主要|
| .text-success |浅绿色(#3c763d) |成功|
| .text-info    | 浅蓝色(#31708) |通知信息|
|.text-warning|黄色(#8a6d3b|警告|
|.text-danger|褐色(#a94442)|危险|
 * 文本对齐

| 类名      | 效果    |
| --------- | -------- |
| .text-left    | 左对齐  |
| .text-center     | 居中对齐   |
| .text-right     | 右对齐 |
| .text-justify | 两端对齐   |

* * *
注：
* 本文学习内容来自于慕课网[《 玩转Bootstrap（基础）》](http://www.imooc.com/learn/141)

