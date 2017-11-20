from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import models

	
# Create your views here.
def index_blog(request):#参数严格意义都可以
	articles=models.Article.objects.all()
	return render(request,'blog/index.html',{'articles':articles})

def article_page(request,article_id):
	article = models.Article.objects.get(pk=article_id)
	return render(request,'blog/articlePage.html',{'article':article})
		
def edit_page(request,article_id):
	if str(article_id)=='0':
		return render(request,'blog/editPage.html')
	else:
		article=models.Article.objects.get(pk=article_id)
		return render(request,'blog/editPage.html',{'article':article})

def edit_action(request):
	title = request.POST.get('title')
	content = request.POST.get('content')
	article_id =request.POST.get('article_id','0')#defaulr :'0'
	if article_id =='0':
		models.Article.objects.create(title=title,content=content)
		return HttpResponseRedirect(reverse('blog:home'))
		#articles=models.Article.objects.all()
		#return render(request,'blog/index.html',{'articles':articles})
	else:
		article=models.Article.objects.get(pk=article_id)
		article.title=title
		article.content=content
		article.save()
		return render(request,'blog/articlePage.html',{'article':article})
			
def delete_page(request,article_id):
	models.Article.objects.get(pk=article_id).delete()
	articles=models.Article.objects.all()
	return render(request,'blog/index.html',{'articles':articles})
	