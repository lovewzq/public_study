# Windows下的[Apache](http://httpd.apache.org/)

## 下载：
![2018-11-20_13-02]($resource/2018-11-20_13-02.png)
![2018-11-20_13-05]($resource/2018-11-20_13-05.png)
![2018-11-20_13-07]($resource/2018-11-20_13-07.png)
## 安装：
1. 解压到想要安装的磁盘：
![2018-11-20_13-10]($resource/2018-11-20_13-10.png)
2. 修改配置文件：`"G:\Apache\conf\httpd.conf"`
* 修改`httpd.conf`文件中的`Define SRVROOT`为`Apache的实际安装路径`
![2018-11-20_13-13]($resource/2018-11-20_13-13.png)
3. 安装Apache主程序：`CMD`（以管理员身份运行）执行：`"G:\Apache\bin\httpd.exe" -k install -n apache`
![2018-11-20_13-23]($resource/2018-11-20_13-23.png)
![2018-11-20_13-25]($resource/2018-11-20_13-25.png)
4. 启动Apache
* 在计算机`服务`里面启动
![2018-11-20_13-30]($resource/2018-11-20_13-30.png)
* 在Apache安装路径下的`bin目录`下打开`ApacheMonitor.exe`启动
![2018-11-20_13-30_0]($resource/2018-11-20_13-30_0.png)
5. 安装成功：浏览器输入`127.0.0.1`看到如下网页
![2018-11-20_13-33]($resource/2018-11-20_13-33.png)

