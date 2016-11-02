
## SSH 端口映射 进程保护

服务器需要开启 ssh-server 服务
客户端需要安装 ssh-client,
- - -
需要配置好公钥到服务器上,配置方法 `ssh-copy-id user@server` 可以直接配置好公钥.
- - -
如果没有`ssh-copy.id`这个工具的话,可以自己进入到 `~/.ssh/id_rsa.pub` 这个是公钥文件,把里面的内容复制到服务器上的 `~/.ssh/known_hosts` 文件里面,这个文件是存放一直登陆账号的文件,记录了之后,用户登陆不需要密码.
- - -
如果在 `~/.ssh/` 目录下没有找到找到公钥文件的话,或者连这个 `.ssh` 文件夹都没有的话,就需要生成密钥.执行 `ssh-keygen` 直接可以生成ssh的rsa算法公钥密钥对.在生成的时候,会要求让你输入密码,你可以不输入,之久回车跳过.

下载这个工具后,在 `configTunnel.py` 中配置好自己的服务器,端口,还有登陆用户,注意需要服务器开启ssh服务,同时登陆用户已经配置好登陆公钥.

配置一下环境变量.然后
运行 `./run` 就可以运行,
在开启系统里面加入 `run` 可以弄成开机自启.

#### 目前还有很多issue:
1. 目前还不稳定
2. 还需要自动配置环境变量
3. 把配置文件写成json文件



============================
May 15
============================
第一个版本
基本功能完成

============================
Wed Aug 17 17:35:41 CST 2016
============================

写入了配置文件模块
可以配置默认端口,服务器用户,服务器地址,域名,间隔时间等参数

============================
Tue Sep  6 15:04:45 CST 2016
============================

重写了进程操作模块,功能基本稳定没有Bug.
可以持续守护管道进程

============================
Wed Sep  7 17:32:09 CST 2016
============================

加入了检查功能,如果main.py一旦存在系统进程中.
自动停止第二个main.py程序

============================
Mon Sep 12 11:01:51 CST 2016
============================

修改了 nohup 最外层的 stderr 重定向错误.
在终端 2>&1 &	2:stderr
				1:stdout
添加rerun脚本, 并脚本放在 ~/.bashrc 每次执行
防止出现主运行脚本 tunnelMain.py 在执行的时候网络中断
使tunnelMain.py已经执行,但是ssh通道执行失败
出现了 ssh<defunct> 进程,这个是ssh执行有错误提示给用户出现的进程
修改main.py 为 tunnelMain.py 


============================
Wed Sep 14 09:45:20 CST 2016
============================

加入日志时间打印
添加网络测试连接,
网络通畅时,建立通道,并休眠interval秒
网络不通时,死循环检测,间隔10s

PS: 修复网络不通时建立通道会让程序崩溃
BUG: 日志输出的时候,标准输出被错误输出给占用了.
	 不能正常标准输出

============================
Wed Sep 14 12:44:46 CST 2016
============================

修复: 杀死已经开启的转发管道BUG

============================
Thu Sep 29 00:40:47 CST 2016
============================

在开启通道间隔interval时间的时候
同时检测网络是否断开,如果端口的话
直接退出interval睡眠
然后关闭通道,下个循环重新开启新通道

防止在开启通道的时候,因为意外网络断开之后
就需要等待interval长的时间才能重新建立通道

============================
Fri Sep 30 00:40:43 CST 2016
============================

修改测试网络时间为10s
并写在configTunnel配置文件里面