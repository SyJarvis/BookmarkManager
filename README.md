# 书签项目

首先说一下本项目的宗旨，我是想建立一个资源管理、检索、分析的平台。收集书签、文档、图片、数据等。但是这个项目只是其中的一部分，仅实现了书签的管理。



## 本项目使用的开发平台

系统：ubuntu18.04

IDE:Pycharm

编程语言：python+HTML+CSS+JS

框架：Django



## 环境安装

```
virtualenv django_2 -p python3
source ./django_2/bin/activate
pip install -r requirements.txt
在此之后，打开yilai文件夹，将haystack文件夹替换掉虚拟环境里/home/ubuntu/django_2/lib/python3.6/site-packages/haystack这个文件夹。
```



#### 建立一个数据库

```
create database bookmark charset=utf8mb4;
将数据导入
source ./bookmark.sql
```



## 启动

```
python manage.py runserver
```





## 效果图

![1](/home/jarvis/Desktop/bookmark_master/书签项目V2/效果图/1.png)

