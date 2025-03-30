from django.shortcuts import render,get_object_or_404,redirect
from bloginterface.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def Home(request):
    queryset = Post.objects.all()
    return render(request, 'index.html', {"posts": queryset})

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category = request.POST.get('category')
        published = request.POST.get('published') == 'on'

        category = None
        if category:
            try:
                category = Category.objects.get(pk=category)
            except Category.DoesNotExist:
                return render(request, 'post_form.html', {'error': 'Invalid category.', 'categories': Category.objects.all()})

        blog = Post.objects.create(
            title = title,
            content = content,
            category = category,
            published = published,
            author = request.user
        )

        return redirect('/')
    categories = Category.objects.all()
    return render(request, 'post_form.html', {'categories': categories})

@login_required
def post_details(request, pk):
    post = get_object_or_404(Post, pk= pk)
    return render(request, 'post_details.html', {'post': post})

@login_required
def post_edit(request, pk):
    details = get_object_or_404(Post, pk=pk)
    categories = Category.objects.all()

    if request.method == 'POST':
        details.title = request.POST.get('title')
        details.content = request.POST.get('content')
        category = request.POST.get('category')
        details.published = request.POST.get('published') == 'on'

        if category:
            try:
                details.category = Category.objects.get(pk=category)
            except Category.DoesNotExist:
                return render(request, 'post_edit.html', {'details': details, 'categories': categories, 'error': 'Invalid category.'})
        else:
            details.category = None

        details.save()
        return redirect('/')
    return render(request, 'post_edit.html', {'details': details, 'categories' : categories})

@login_required
def post_delete(request, pk):
    detail = get_object_or_404(Post, pk=pk)
    detail.delete()

    return redirect('/')