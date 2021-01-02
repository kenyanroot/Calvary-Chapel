from django.shortcuts import render
from django.utils import timezone
from django.views.generic import DetailView,ListView

from .models import Blog, Category, FeaturedPosts


# Create your views here.

featuredlist=[]
class BlogClass(ListView):
    template_name = 'blog.html'
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.all()
        featuredmain = FeaturedPosts.objects.latest('title', 'short_description', 'category', 'article_thumbnail')
        for featured in FeaturedPosts.objects.all():
            featuredlist.append(featured)
            print(featuredlist)

        context['category']=category
        context['featuredlist']=featuredlist
        context['featuredmain']=featuredmain

        return context



def blog(request):
    myblog = Blog.objects.all()
    category = Category.objects.all()
    featuredmain = FeaturedPosts.objects.latest('title','short_description','category','article_thumbnail')

    for featured in FeaturedPosts.objects.all():
        featuredlist.append(featured)
        print(featuredlist)


    context = {

        'myblog': myblog,
        'category': category,
        'featuredlist': featuredlist,
        'featuredmain':featuredmain,

    }

    return render(request, 'blog.html', context)


class Blogpost(DetailView):
    template_name ='postdetail.html'
    model = FeaturedPosts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.all()
        featuredmain = FeaturedPosts.objects.latest('title', 'short_description', 'category', 'article_thumbnail')
        for featured in FeaturedPosts.objects.all():
            featuredlist.append(featured)
            print(featuredlist)

        context['category'] = category
        context['featuredlist'] = featuredlist
        context['featuredmain'] = featuredmain


        return context

def st(request):
    return render(request,'postdetail.html')



def search(request):
    if request.method=='POST':

        keyword=request.POST['keyword']
        results=Blog.objects.filter(category__contains=keyword)
        print(keyword,results)
        totalresults=results.count()

        context={

            'results':results,
            'totalresults':totalresults

        }

        return render(request,'searchresults.html',context)

    else:
        return render(request, 'searchresults.html')

