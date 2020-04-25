from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Post
from django.shortcuts import redirect
# Create your views here.

def homepage(request):
	posts = Post.objects.all()
	now = datetime.now()
	# for count, post in enumerate(posts):
	# 	post_lists.append("No. {}:".format(str(count)) + str(post.title) + "<br>" + str(post.slug) + "<br>")
	# 	post_lists.append("<small>" + str(post.body.encode('utf-8')) + "</small><br><br>")
	#return HttpResponse(post_lists)
	return render(request, 'index.html', locals())

def showpost(request, slug):
	try:
		post = Post.objects.get(slug = slug)
		if post != None:
			return render(request, 'post.html', locals())
	except:
		return redirect('/')