# Pornhub爬虫

## 一个可以获取Pornhub视频和Cover的爬虫程序
### 发布时间：2020.05.23

### 环境&模块:

#### 开发环境：Python3 Win10 PyCharm
#### 测试环境：Win10  Ubuntu  Centos  Debian
#### 模块：re，requests，lxml，time，os

### 实现功能：
- 所有下载视频均为最高清晰度
- 解析单个视频真实链接
	- 输出真实链接
	- 选择是否下载
- 解析某个页面所有视频真实链接 可批量下载
- 保存视频到相应标题目录下mp4文件以当日时间命名
- 保存封面到相应标题目录下jpg文件以Cover命名

## 使用：

### Python3环境
**Centos:**
```shell
yum install python3 pip3 -y
```
**Debian:**
```shell
apt-get install python3 pip3 -y
```
**Ubuntu:**
```shell
sudo apt-get install python3 pip3 -y
```


### 模块安装&项目拉取

**1.安装所需模块**
```shell
pip3 install requests lxml
```

**2.拉取项目**
```shell
git clone https://github.com/moeik/PornhubSpider.git && cd PornhubSpider
```

**3.运行**
python3 app.py

### 目录结构：
```
|——Pornhub
|   |——{title}
|      |——{time}.mp4
|      |——Cover.jpg
```

### 声明：
- 本项目只是个人爬虫初上手项目，代码较乱吗，大佬勿喷。
- 练手项目难避免有很多Bug，也欢迎提交Bug，在能力范围内进行改进。
- 欢迎大家Star。