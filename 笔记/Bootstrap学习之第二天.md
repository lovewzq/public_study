# Bootstrp学习之第二天

### 列表
* 无序列表，有序列表

```html
<!--无序列表-->
<ul>
<li>列表一</li>
</ul>
<!--有序列表-->
<ol>
<li>列表二</li>
</ol>
```

* 去点列表(无序列表添加类名：==list-unstyled==)

```html
<!--无点列表-->
<ul class="list-unstyled">
<li>列表一</li
</ul>
```

* 内联列表(无序列表添加类名：==list-inline==):垂直列表变成水平列表
```html
<!--内联列表-->
<ul class="list-inline">
<li>列表</li>
</ul>
```

* 定义列表：
```html
<dl>
<dt>列表一</dt>
</dl>
```

* 水平定义列表(添加类名：==dl-horizontal==)
```html
<dl class="dl-horizontal">
<dt>列表</dt>
<dd>列表一</dd>
</dl>
```

### 代码
* 单行列表代码<code>
* 多行代码<pre>
* 显示用户输入代码<kbd>
* <pre>添加类名==pre-scrollable==

### 表格
* 基础表格添加==table类名==
* 斑马线表格添加==table-striped类名==
* 带边框的表格==table-borderd类名==
* 鼠标悬停高亮的表格==table-hover==
* 紧凑型表格==table-condensed==
* 响应式表格==table-responsive==
```html
<table class="table table-striped table-bordered table-hover">
   <thead>
     <tr>
       <th>表格标题</th>
     </tr>
   </thead>
   <tbody>
     <tr>
       <td>表格单元格</td>
     </tr>
     <tr>
       <td>表格单元格</td>
     </tr>
     <tr>
       <td>表格单元格</td>
     </tr>
     <tr>
       <td>表格单元格</td>
     </tr>
   </tbody>
 </table>
 <h1>紧凑型表格</h1>
  <table class="table table-condensed">
   <thead>
     <tr>
       <th>表格标题</th>
     </tr>
   </thead>
   <tbody>
     <tr>
       <td>表格单元格</td>
     </tr>
     <tr>
       <td>表格单元格</td>
     </tr>
     <tr>
       <td>表格单元格</td>
     </tr>
     <tr>
       <td>表格单元格</td>
     </tr>
   </tbody>
 </table>
 <h1>响应式表格</h1>
 <div class="table-responsive">
   <table class="table table-bordered">
   <thead>
     <tr>
       <th>表格标题</th>
     </tr>
   </thead>
   <tbody>
     <tr>
       <td>表格单元格</td>
     </tr>
     <tr>
       <td>表格单元格</td>
     </tr>
     <tr>
       <td>表格单元格</td>
     </tr>
     <tr>
       <td>表格单元格</td>
     </tr>
   </tbody>
 </table>
</div>
```


