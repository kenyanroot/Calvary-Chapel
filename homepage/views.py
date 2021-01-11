from django.shortcuts import render,HttpResponse
from blog.models import Blog
from  homepage.models import Grid,PastorsQuote
# Create your views here.

def index(request):
    posts=Blog.objects.all()
    grid=Grid.objects.all()
    pastors_quote=PastorsQuote.objects.all()
    context={
        'posts':posts,
        'grid':grid,
        'pastors_quote':pastors_quote,
    }

    return render(request,'index.html',context)


def youth(request):
    return render(request,'youth.html')


def location(request):
    return render(request,'location.html')


def about(request):
    return render(request,'about.html')


def calvaryLearningCenter(request):
    return HttpResponse('coming soon!')


# def index(request):
#     return render(request,'index.html')
#
