from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return render(request, 'website/index.html')

def single_view(request):
    return render(request, 'website/single.html')

def slidbar_view(request):
    return render(request, 'website/slidbar.html')

def blog_view(request):
    return render(request, 'website/blog.html')
