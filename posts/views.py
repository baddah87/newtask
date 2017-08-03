from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404

# Create your views here.


def post_create(request):
	return render (request, 'post_create.html', {})

def post_detail(request):
	instance= Post.objects.get(id=1)
	context={
	"title": "Detail",
	"instance": instance,
	}
	return render (request, 'post_detail.html', context)

def post_list(request):
	object_list= Post.objects.all()
	context={
	"object_list": object_list,
	"title": "List",
	"user": request.user,
	}
	return render (request, 'post_list.html', context)

def post_update(request):
	return HttpResponse ("<h1>Hello</h1>")

def post_delete(request):
	return HttpResponse ("<h1>Hello</h1>")