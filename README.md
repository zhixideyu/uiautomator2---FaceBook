# uiautomator2---FaceBook
**uiautomator2**是一个可以使用Python对Android设备进行UI自动化的库。其底层基于Google uiautomator。
 
- **功能丰富** ：设备和开发机可以脱离数据线，通过WiFi互联；
- **得心应手** ：集成了openstf/minicap加快截图速度, 集成了openstf/minitouch达到精确实时控制设备, 修复了xiaocong/uiautomator经常性退出的问题；
- **深度整合** ：代码进行了重构和精简，方便维护。



## uiautomator2---FaceBook简介
 该项目是使用uiautomator2作为测试开发工具, 来自动化操控FaceBook以及其它的一些app.   —— [uiautomator2项目原址](https://github.com/openatx/uiautomator2)
 
 **下面是该项目开始前的准备步骤**
>**一. 安装adb**

**adb**, 即Android Debug Bridge,它是Android开发/测试人员不可替代的强大工具,具体内容自行百度.

    1.下载adb工具

      将文件名称中含有adb的文件和fastboot.exe复制到C:/windows/system32目录

      将文件名称中含有adb的所有文件复制到C:/windows/system目录

      将文件名称中含有adb的所有文件复制到C:/windows/SysWoW64目录

      win7与win10同样使用，其他win版本没有操作过，未知！

注意: 一定要将所对应的文件全部复制到指定目录中
>**二. 测试adb**

    1. 打开cmd命令行输入adb
    
    2. 查看adb版本: adb version
>**三. uiautomator2安装**

    1. cmd命令行输入

       pip install --pre uiautomator2

       或者

       git clone https://github.com/openatx/uiautomator2

       pip install -e uiautomator2

       pip install pillow

    2. 当你的adb工具已经安装完成后,并且在cmd中可以启动服务,同时你的电脑连接上一个手机或多个手机或虚拟机

       注意: 需要打开设备的开发者模式,不同品牌手机的开发者模式打开方式上网查询即可

       在cmd命令行输入

       python -m uiautomator2 init

       或者指定单个设备

       python -m uiautomator2 init --serial $SERIAL

这时命令会自动安装本库所需要的设备端程序,也会在你的手机里安装两个软件一个可见一个不可见(有图标和没图标)手动点击安装即可

**最后安装提示success即可**

**注意**：如果在操作的过程当中提示 no module xxx,可自行对照安装即可,如果出现其它情况请自行百度(祝好运!)
>**四. 测试连接**

    1. 在cmd命令行中输入
    
    2. adb devices
    
    3. 测试是否与手机连接成功
emulator-5554: 你连接设备的序列号
出现以上内容则表明已连接成功,如果出现其情况自行百度(祝好运!)
>**五. 可视化UI查看器**

    安装 pip install --pre -U weditor
    
    在cmd命令行中输入
    
    python -m weditor
    
    会自动打开一个浏览器

**这样,使用uiautomator2的前期基本操作就完成了,接下来就是写python脚本来自动化的操作android上app程序.**
## 项目所需
- **app** ：FaceBook，VirtualApp，uiautomator。
- **网络环境** ：需要访问外网。
- **平台**：需要一个手机打码平台，也可以使用自己手机号注册。 
- **安卓手机**：需要一个安卓版本在6.0.0以上的 手机（才能使用该项目的Facebook的版本）。

**https://www.apkhere.com/** 该网站可以下载任何版本的Facebook，此项目使用的是 Facebook 165.0.0.53.93的版本。[点击下载](https://www.apkhere.com/down/com.facebook.katana_165.0.0.53.93_free)

**VirtualApp**：是一个App虚拟化引擎，创建了一个虚拟空间，你可以在虚拟空间内任意的安装，启动和卸载APK， 这一切都与外部隔离，如同一个沙盒。该项目我在里面安装5个Facebook。

## 手机参数

| 手机型号      |    机身存储 | 运行内存| MIUI版本|处理器|Android版本|

| :-------- | --------:| :--: |

| Redmi4X  | 16.00GB |  2.00GB |9.5.3.0|八核|7.1.2|

