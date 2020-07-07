# ROS学习笔记

### 一、ROS简介

#### 1.1 ROS对于智能机器人的意义

​	在讨论这个问题前，不妨先考虑另一个问题，Android 系统对智能手机的意义是什么？Android 系统带给手机的功能甚至可以在单片机上实现，事实上在智能手机出现之前的功能机就是这么做的。那为什么现在近乎所有除苹果以外的手机都搭载了 Android 系统呢？

​	原因其实很简单，Android 为手机的开发提供了一个标准，这个统一的标准的好处在于可以让大量的第三方开发团队得以在同一标准下进行开发，而不用担心自己开发出来的软件与大部分的手机都不兼容，这就让每个团队都可以发挥自己的长处，譬如 A 厂商擅长造轮子，B 厂商和 C 厂商擅长造车架，A 厂商根据统一的业内标准制造出既优质，又能同时匹配 B 厂商和 C 厂商制造的轮子，那就不会让已经购买了车架的人因无法匹配 A 厂商的轮子而放弃这一优质的车轮。与此同时，若 A 厂商不擅长做其它的车部件，也不必为其担心，因为 A 厂商只需要在自己擅长的领域进行开发，而不需要担心自己造的轮子不匹配其它厂商制造的车架。

​	**ROS对于机器人的意义也是这般，它提供了一个标准的框架，使得大量的第三方开发团队可以在其上开发而不用过多担心开发之外的东西，例如各个模块之间的通讯问题等等。**

#### 1.2 安装ROS

1.2.1 [ROS wiki](http://wiki.ros.org/ROS/Installation)

	>系统：Ubuntu 16.04
	>
	>ROS版本：Kinetic

1.2.2 设置ROS源

> **`sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'`**

1.2.3 设置密钥

> **`sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654`**

1.2.4 安装

> 首先更新源
>
> **`sudo apt-get update`**
>
> 安装完整的 kinetic 版本
>
> **`sudo apt-get install ros-kinetic-desktop-full`**

1.2.5 环境设置

> **`echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
> source ~/.bashrc`**

1.2.6 安装 rosinstall 、rosdep

> 安装 rosinstall
>
> **`sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential`**
>
> 安装 rosdep
>
> **`sudo apt install python-rosdep`**
>
> 测试 rosdep
>
> **`sudo rosdep init`**
>
> 初始化 rosdep 出现 **cannot download default sources list from:【closed】**错误解决方案
>
> 打开hosts文件
>
> **`sudo gedit /etc/hosts`**
>
> 在文件末尾添加
>
> **`151.101.84.133  raw.githubusercontent.com`**
>
> 保存退出后重新尝试
>
> **`sudo rosdep init`**
>
> **`rosdep update`**

### 二、



