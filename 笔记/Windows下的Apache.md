# Windows下的[Apache](http://httpd.apache.org/)

## 下载：
![2018-11-20_13-02](https://websit-resource.oss-cn-hangzhou.aliyuncs.com/2018-11-20_13-02.png?OSSAccessKeyId=LTAIViILYGCEqYDj&Expires=1579489187&Signature=dlARK0GBgNDDIN%2BqbpmL2%2FnDxTU%3D)

![2018-11-20_13-05](https://websit-resource.oss-cn-hangzhou.aliyuncs.com/2018-11-20_13-05.png?OSSAccessKeyId=LTAIViILYGCEqYDj&Expires=5143489215&Signature=aBaapdshEXWeuRYk5%2BDrJ7ai2QI%3D)
![2018-11-20_13-07](https://websit-resource.oss-cn-hangzhou.aliyuncs.com/2018-11-20_13-07.png?OSSAccessKeyId=LTAIViILYGCEqYDj&Expires=37543489249&Signature=W%2B8GQR3nvGB0vZ3%2F3AaHm%2BAyDrk%3D)
## 安装：
1. 解压到想要安装的磁盘：
![2018-11-20_13-10](https://websit-resource.oss-cn-hangzhou.aliyuncs.com/2018-11-20_13-10.png?OSSAccessKeyId=LTAIViILYGCEqYDj&Expires=5143489266&Signature=A9EmjndqZZNAYmGayDDtM19%2FImE%3D)
2. 修改配置文件：`"G:\Apache\conf\httpd.conf"`
* 修改`httpd.conf`文件中的`Define SRVROOT`为`Apache的实际安装路径`
![2018-11-20_13-13](https://websit-resource.oss-cn-hangzhou.aliyuncs.com/2018-11-20_13-13.png?OSSAccessKeyId=LTAIViILYGCEqYDj&Expires=37543489288&Signature=k%2BzhaJsPTsXiblPo5R8gvo3lQYE%3D)
3. 安装Apache主程序：`CMD`（以管理员身份运行）执行：`"G:\Apache\bin\httpd.exe" -k install -n apache`
![2018-11-20_13-23](https://websit-resource.oss-cn-hangzhou.aliyuncs.com/2018-11-20_13-23.png?OSSAccessKeyId=LTAIViILYGCEqYDj&Expires=5143489347&Signature=MmWeMTsXn3Yg7iuLNlA7Nsv47Mc%3D)
![2018-11-20_13-25](https://websit-resource.oss-cn-hangzhou.aliyuncs.com/2018-11-20_13-25.png?OSSAccessKeyId=LTAIViILYGCEqYDj&Expires=37543489382&Signature=Ie7fWcFzc%2Bcl1MK%2BC5Vt4WAh5tM%3D)
4. 启动Apache
* 在计算机`服务`里面启动
![2018-11-20_13-30](https://websit-resource.oss-cn-hangzhou.aliyuncs.com/2018-11-20_13-30.png?OSSAccessKeyId=LTAIViILYGCEqYDj&Expires=37543489401&Signature=Gc%2FqFzQJsXhL4xxX863DOyfqvYE%3D)
* 在Apache安装路径下的`bin目录`下打开`ApacheMonitor.exe`启动
![2018-11-20_13-30_0](https://websit-resource.oss-cn-hangzhou.aliyuncs.com/2018-11-20_13-30_0.png?OSSAccessKeyId=LTAIViILYGCEqYDj&Expires=37543489427&Signature=YYQ5t3DQhGRyWs7nkXMYwkjaYeg%3D)
5. 安装成功：浏览器输入`127.0.0.1`看到如下网页
![2018-11-20_13-33](https://websit-resource.oss-cn-hangzhou.aliyuncs.com/2018-11-20_13-33.png?OSSAccessKeyId=LTAIViILYGCEqYDj&Expires=37543489451&Signature=I8OwhoFH0vD7TdRKukGLwePZvCk%3D)

