from django.conf.urls import url
from . import views
urlpatterns = [
		url(r'^$',views.index_blog,name="home"),
		url(r'^article/(?P<article_id>[0-9]+)$',views.article_page,name='article_index'),
		url(r'^edit/(?P<article_id>[0-9]+)$',views.edit_page,name='edit_page'),
		url(r'^edit/action\/*$',views.edit_action,name='edit_action'),
		url(r'^delete/(?P<article_id>[0-9]+)$',views.delete_page,name='delete_page'),
		
]