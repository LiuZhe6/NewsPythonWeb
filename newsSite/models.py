# coding=utf-8
from django.db import models

# Create your models here.
'''
发布者 发布者头像  1:1
发布者 新闻  1：N
新闻  读者  M：N
新闻  资源  1：N
读者  读者头像    1:1
'''


# 1.发布者
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    sex = models.CharField(max_length=4)
    signature = models.CharField(max_length=80)

    class Meta:
        db_table = 'publisher'


# 2.发布者头像
class PubHeader(models.Model):
    id = models.OneToOneField(Publisher, on_delete=models.CASCADE, primary_key=True)
    url = models.CharField(max_length=40)  # 暂定字符类型

    # 发布者头像和发布者是1:1的关系，这种关系要通过主键来映射

    class Meta:
        db_table = 'pubheader'


# 3.新闻表
class NewModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80)
    type = models.CharField(max_length=16)
    time = models.DateTimeField()
    content = models.TextField()
    # 给新闻表添加一个外键属性
    # 参数表：
    # Publisher：从表关联的那张主表
    # 第二个：当主表的记录删除了，同时也把从表中相应的记录删除
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)  # 当主表的某条记录删除了

    class Meta:
        db_table = 'newsmodel'


# 4.读者
class Reader(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=20)
    nickname = models.CharField(max_length=40)
    sex = models.CharField(max_length=4)
    signature = models.CharField(max_length=50)

    class Meta:
        db_table = 'reader'


# 5.关系表 (读者和新闻之间有着 M : N的关系)
class Browse(models.Model):
    # 关系表依从于读者表和新闻表
    #    依从读者表，将读者的主键设置为 关系者的外键
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    # 依从于新闻表，将新闻的主键设置为关系表的外键
    news = models.ForeignKey(NewModel, on_delete=models.CASCADE)
    # 注意 ： 关系表不需要设置主键
    # 态度
    # -1 代表踩  0没态度 1赞
    attitude = models.IntegerField()
    comment = models.TextField()

    class Meta:
        db_table = 'browse'


# 6.资源
class Source(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=30)
    # 资源依从于新闻，是1：N的关系
    news = models.ForeignKey(NewModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'source'


# 7.读者头像
class ReaderHeader(models.Model):
    id = models.OneToOneField(Reader, on_delete=models.CASCADE, primary_key=True)
    url = models.CharField(max_length=40)

    class Meta:
        db_table = 'readerHeader'
