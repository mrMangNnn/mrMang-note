## lubuntu18.04安装Typora与Markdown入门

* **安装Typora**

  获得密钥

  ​	`wget -qO - https://typora.io/linux/public-key.asc | sudo apt-key add -`

  或

  ​	`sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BA300B7755AFCFAE`

  加入Typora源

  ​	`sudo add-apt-repository 'deb https://typora.io/linux ./`

  ​	`sudo apt-get update`

  安装

  ​	`sudo apt-get install typora`

* **Markdown**

  ​	[原文地址](https://www.jianshu.com/p/1e402922ee32)

  1. 目录树

     `[toc]  #标题都会被捕获到目录中`

  2. 标题

     `在文字前加#即可(记得加空格)`

  3. 列表

     `用-或*加空格变为无序列表,用1. 2. 3.等加空格变为有序列表`

  4.  引用

     在文本前加>即可

  5. 图片与链接

     `图片： ![]() 链接：  []()`

     `在[]中输入图片或链接的名字,()中输入链接`

  6. 粗体与斜体

     `用两个*包含文本即可变成粗体,用一个*包含文本即可变成斜体`

  7. 表格

     `用|连接表格即可`

  8. 分割线

     `三个*号即可`

     

     