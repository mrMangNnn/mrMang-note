## git tutorial

[原文地址](https://www.liaoxuefeng.com/wiki/896043488029600)

***

* **在Linux上安装git**

  `sudo apt-get install git`

  

* **创建版本库(repository)**

  1. 新建一个文件夹
  2. `git init  #初始化文件夹`

  

* **基本操作**

  1. `git add name  #添加一个名为name的文件到本次修改`
  2. `git commit -m '注释'  #提交当前的所有修改到仓库`
  3. `git status  #查看目前仓库的状态(可以查看有无添加修改，提交修改)`
  4. `git log  #查看历史记录,加上--pretty = oneline可以减少不必要的输出信息`
  5. `git reflog  #查看每一次命令(含commit id)`
  6. `git HEAD^  #回到上一个版本,即上一次提交,可以用HEAD~100来回到前100个版本`
  7. `git reset --hard 12345  #回到某个版本,12345指对应版本的commit id前几位 `
  8. `git checkout -- name  #撤销工作区的修改`
  9. `git reset HEAD name  #撤销暂存区的修改`
  10. `git rm name  #删除版本库中名为name的文件(记得commit保存)`

  

* **分支**

  1. `git branch  #查看当前分支`
  2. `git branch name  #创建名为name的分支`
  3. `git checkout name  #切换到名为name的分支`
  4. `git merge name  #将名为name的分支合并到当前分支`
  5. `git branch -d name  #删除名为name的分支`
  6. `git stash  #储藏当前工作,使目前分支的修改不影响到其他分支`
  7. `git stash list  #查看储藏的工作`
  8. `git stash pop  #恢复并删除储藏的工作`
  9. `git stash apply  #恢复并保留储藏的工作`

  

* **搭建远程仓库**

  1. 创建`SSH Key`

     `ssh-keygen -t rsa -C "yourEmail@example.com"`

  2. 找到`.ssh`目录,打开`id_rsa.pub`复制其中的内容

  3. 登录`github`,打开`setting`后找到`SSH Keys`页面粘贴`id_rsa.pub`文件中的内容

  

* **操作`github`仓库**

  1. 连接：

     `git remote add origin git@github.com:youName/niubi.git`

  2. 传输：

     `git push -u origin master  #首次`

     `git push origin master`

  3. 从远程库克隆到本地库：

     `git clone git@github.com:youName/niubi.git`

  

