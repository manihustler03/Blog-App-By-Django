from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserLoginForm,CategoryForm
from .models import BlogPost

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'blog/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        category=request.POST['category']
        BlogPost.objects.create(title=title, content=content, author=request.user,category=category)
        return redirect('home')
    form=CategoryForm()
    return render(request, 'blog/create_post.html',{'form':form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('home')
    return render(request, 'blog/edit_post.html', {'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'blog/delete_post.html', {'post': post})

def home(request):
    posts = BlogPost.objects.all()
    reversePost=posts[::-1]
    return render(request, 'blog/home.html', {'posts': reversePost,'tech':'Tech','cinema':'Cinema','news':'News','sports':'Sports'})
@login_required
def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    post_category=post.category
    allPosts=BlogPost.objects.all()
    return render(request, 'blog/post_detail.html', {'post': post,'allPosts':allPosts,'post_category':post_category})

def Category_Tech(request):
    category = BlogPost.objects.filter(category="Tech")
    return render(request, 'blog/category.html', {'category': category,'name':'Tech'})
def Category_Cinema(request):
    category = BlogPost.objects.filter(category="Cinema")
    return render(request, 'blog/category.html', {'category': category,'name':'Cinema'})
def Category_News(request):
    category = BlogPost.objects.filter(category="News")
    return render(request, 'blog/category.html', {'category': category,'name':'News'})
def Category_Sport(request):
    category = BlogPost.objects.filter(category="Sports")
    return render(request, 'blog/category.html', {'category': category,'name':'Sports'})

def Category(request, name):
    if name is not None:
        category = BlogPost.objects.filter(category=name)
        return render(request, 'blog/category.html', {'category': category, 'name': name})
    else:
        # Handle the case where name is None, maybe redirect or show an error
        return render(request, 'blog/category.html', {'error': 'No category specified'})