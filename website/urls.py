from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', index_view, name='index'),
    path('single', single_view, name='single'),
    path('slidbar', slidbar_view, name='slidbar'),
    path('blog', blog_view , name='blog')
]
