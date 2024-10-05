from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm, RegisterForm  # Crea estos formularios
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

# blog/views.py

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comment_set.all()
    comment_form = CommentForm()
    
    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post_id)
    
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })
@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})
def post_list(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    
    # Filtrar por categoría
    category_id = request.GET.get('category')
    if category_id:
        posts = posts.filter(category_id=category_id)
    
    # Filtrar por antigüedad
    order = request.GET.get('order')
    if order == 'desc':
        posts = posts.order_by('-created_at')
    elif order == 'asc':
        posts = posts.order_by('created_at')
    elif order == 'alpha':
        posts = posts.order_by('title')

    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories})
# blog/views.py

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})
# blog/views.py

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})
# blog/views.py

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category)
    return render(request, 'blog/category_detail.html', {'category': category, 'posts': posts})
def about(request):
    return render(request, 'blog/about.html')
# blog/views.py

def contact(request):
    return render(request, 'blog/contact.html')
