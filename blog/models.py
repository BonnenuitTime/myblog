from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField


# 博客分类
class Category(models.Model):
    name = models.CharField('博客分类', max_length=100)
    index = models.IntegerField(default=100, verbose_name='分类排序')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章标签
class Tag(models.Model):
    name = models.CharField('文章标签', max_length=100)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 推荐表
class Recommend(models.Model):
    name = models.CharField('推荐位', max_length=100)

    class Meta:
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章
class Article(models.Model):
    title = models.CharField('标题', max_length=70)
    digest = models.CharField('摘要', max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='分类', blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    img = models.ImageField(upload_to='article/%Y/%m/%d/', verbose_name='文章图片', blank=True, null=True)
    body = UEditorField('内容', width=800, height=500, toolbars="full", imagePath="uping/"
                        , filePath="upfile/", upload_settings={"imageMaxSize": 1204000}, settings={},
                        command=None, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    views = models.PositiveIntegerField('阅读量', default=0)
    recommend = models.ForeignKey(Recommend, on_delete=models.DO_NOTHING, verbose_name='推荐位', blank=True, null=True)
    creat_time = models.DateTimeField('创建时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# Banner
class Banner(models.Model):
    text_info = models.CharField('图片标题', max_length=50, default='')
    img = models.ImageField(upload_to='banner/', verbose_name='轮播图')
    link_url = models.URLField(verbose_name='图片链接', max_length=100)
    is_active = models.BooleanField('是否显示', default=False)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text_info




# 友情链接
class Link(models.Model):
    name = models.CharField('链接名称', max_length=50)
    link = models.URLField('链接地址', max_length=100)

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# Create your models here.