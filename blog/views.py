from django.shortcuts import render
from django.http import HttpResponse
from . import models

	
# Create your views here.
def index(request):#参数严格意义都可以
	article=models.Article.objects.get(pk=1)
	return render(request,'blog/index.html',{'hello':'Hello blog','article':article})