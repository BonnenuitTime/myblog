from django.contrib import admin
from .models import Banner,Category,Recommend,Article,Tag,Link


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','category','title','recommend','user','views','creat_time')
    list_per_page = 50
    ordering = ('-creat_time',)
    list_display_links = ('id','title')
    # list_editable = ('category','recommend','title')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id','text_info','link_url','is_active')
    list_editable = ('text_info','link_url','is_active')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_editable = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','index')
    list_editable = ('name',)


@admin.register(Recommend)
class RecommendAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_editable = ('name',)


@admin.register(Link)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id','name','link')
    list_editable = ('name','link')




# Register your models here.
