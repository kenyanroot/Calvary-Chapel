from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')


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
