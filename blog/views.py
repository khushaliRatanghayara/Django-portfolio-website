from django.shortcuts import render,get_object_or_404
from .models import Blog
from django.shortcuts import render

# Create your views here.

def bloglist(request):
    BlogObj = Blog.objects
    return render(request,'bloglist.html',{'blogs':BlogObj})

def blog_details(request,blog_id):
    detail_blog = get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'details':detail_blog})


