
from django.shortcuts import get_object_or_404, render
from .models import Posts

# Create your views here.
def all_blogs(request):
    
    posts = Posts.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html',{'posts':posts})


def detail(request, post_id):
    post=get_object_or_404(Posts, pk=post_id)
    return render(request, 'blog/detail.html',{'post':post})
