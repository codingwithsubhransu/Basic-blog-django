from django.shortcuts import render
from bloginterface.models import *

# Create your views here.
def Home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {"posts": posts})

def create_post(request):
    return render(request, 'post_form.html')