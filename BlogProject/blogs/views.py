from django.shortcuts import render, redirect
from . models import Blog
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def blog_post(request):

    blogs = Blog.objects.all().order_by('date')


    all_post = Paginator(blogs,3)
    page = request.GET.get('page')

    try:
        posts = all_post.page(page)
    except PageNotAnInteger:
        posts = all_post.page(1)
    except EmptyPage:
        posts = all_post.page(all_post.num_pages)




    return render(request,'blogs/blog.html',{'blogs':blogs,'posts':posts,'page':page})

def blog_detail(request, slug):
    blogs = Blog.objects.all()


    for blog in blogs:

        if blog.slug == slug:
            return render(request,'blogs/blog_detail.html',{'blog':blog})
    else:
        return HttpResponse('<h1>Such Blog Does Not Exist!</h1>')

@login_required(login_url='/accounts/login/')
def blog_create(request):

    if request.method == 'POST':
        form = forms.CreateBlog(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blogs:blog_post')
    else:
        form = forms.CreateBlog()
    
    return render(request,'blogs/blog_create.html',{'form':form})
    

