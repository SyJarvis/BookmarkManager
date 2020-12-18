bookmark项目配置环境时出现的错误



1.

```
django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3.
```

```
数据库驱动版本出现错误，django2.0开始使用的是mysqlclient，我使用的是pymysql，所以需要注释掉判断版本的语句。
vim /home/ubuntu/django_2/lib/python3.6/site-packages/django/db/backends/mysql/base.py

#if version < (1, 3, 13):
#    raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__v
ersion__)

注释掉判断版本的语句。
```



2.

```
  "/home/ubuntu/dj_bookmarkmanager/lib/python3.6/site-packages/django/db/backends/mysql/operations.py", line 146, in last_executed_query
  query = query.decode(errors='replace')
AttributeError: 'str' object has no attribute 'decode'
```

```
vim /home/ubuntu/django_2/lib/python3.6/site-packages/django/db/backends/mysql/operations.py

跳转到第146行
将decode改为encode
```

