from django.contrib import admin

# Register your models here.
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
	list_display=('title','content','pub_time')
	list_filter=('pub_time',)

admin.site.register(Article,ArticleAdmin)#在admin管理中显示多列
