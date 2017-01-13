首先在本地创建ssh key;

$ ssh-keygen -t rsa -C "your_email@yourmail.com"
后面的your_email@yourmail.com改为你的github上注册的邮箱，之后要求确认路径和输入密码，我们这使用默认的一路回车就行。成功的话会在~/下生成.ssh文件夹，打开文件夹内id_rsa.pub, 复制里面的key。
回到github，进入Account Settings（账户设置）， 左边选择SSH Keys, ADD SSH Key, title随便填，粘贴在你电脑上生成的key，保存。

为了验证是否成功，在git bash下输入：
$ ssh -T git@github.com

出现 “Hi XXXXX! You've successfully authenticated, but GitHub does not provide shell access.”  即表示认证成工，', but GitHub does not provide shell access.'不用理会

$ git clone https://github.com/PythonSelf-studyGroup/MySimpleBlog.git

'''
Cloning into 'MySimpleBlog'...
remote: Counting objects: 6, done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 6 (delta 0), reused 3 (delta 0), pack-reused 0
Unpacking objects: 100% (6/6), done.
Checking connectivity... done.'''

$ git checkout dev #检出dev分支的代码
