# MySimpleBlog 项目说明

关于项目，主要以《Flask Web 开发：基于Python的Web应用开发实战》一书内博客项目为原型，群员共同开发出一个类似的博客项目。练手学习巩固为主，结果为辅，大家尽可施展自己所学知识，给群员以分享，亦或向群员学习探讨。最后达到共同进步的效果。

## 项目骨架

为兼顾大家的基础以及进度，项目骨架采用《Flask Web 开发：基于Python的Web应用开发实战》一书内的项目骨架.

```
├──config.py
├──manage.py
├──migrations/
│  ├── alembic.ini
│  ├── env.py
│  ├── README
│  ├── script.py.mako
│  └── versions/
│  README.md
│  requirements.txt
│  venv/
└──Blog
   ├── auth/ # 对应蓝图
   ├── decorators.py
   ├── email.py
   ├── __init__.py
   ├── main/
   ├── models.py
   ├── static/
   └── templates
... # 其他扩展
```

## 项目功能模块

暂且就书内博客项目功能为基础，大家可自行进行相应扩充

## 项目(Python)编码风格

编码风格应尽量遵守[PEP8](https://www.python.org/dev/peps/pep-0008/)编码规范, 具体大家可自行查看及实践, 望尽量让变量名函数名类名模块名等有意义，不随意取名，变量函数采用下划线命名法，类/异常采用驼峰命名法，以四个空格为一个缩进，适当添加注释。一行宜80-100字符。

## 如何管理代码

我们使用Git来统一管理代码，项目分两个分支，master 和 dev,大家在dev分支进行开发，指定一或两个人对代码进行审查以及合并到master分支

### Git 协作流程

```
$ git clone git@github.com:PythonSelf-studyGroup/MySimpleBlog.git
$ cd MySimpleBlog
$ git branch -a
$ # 在dev分支开发时，可直接在dev分支上开发，也可在dev上再新建分支，再合并至dev分支,需自行选择
$ git branch dev origin/dev
$ git checkout dev
$ git checkout -b my_branch
$ git branch -a
$ # 进行开发
$ # 开发前
$ git pull
$ # 更新分支，解决冲突
```

## 最后

hava a good time
