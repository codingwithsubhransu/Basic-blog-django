from django.shortcuts import render,get_object_or_404
from bloginterface.models import *

# Create your views here.
def Home(request):
    queryset = Post.objects.all()
    return render(request, 'index.html', {"posts": queryset})

def create_post(request):
    return render(request, 'post_form.html')


def post_details(request, pk):
    post = get_object_or_404(Post, pk= pk)
    return render(request, 'post_details.html', {'post': post})