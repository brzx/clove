from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.contrib import messages
from .models import Post
from myauth.models import User
from myauth import views as authview

# Create your views here.
def home(request):
    context = {}
    if 'userid' in request.session:
        context['users'] = User.objects.get(pk=request.session['userid'])
    return render(request, 'home.html', context=context)

def index(request):
    context = {}
    context['posts'] = Post.objects.all()
    if 'userid' in request.session:
        context['users'] = User.objects.get(pk=request.session['userid'])
    return render(request, 'blog/index.html', context=context)

@authview.login_required
def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        error  = None

        if not title:
            error = 'Title is required.'
        if error is not None:
            messages.add_message(request, messages.INFO, error)
        else:
            Post.objects.create(title=title, 
                                body=body, 
                                user=User.objects.get(pk=request.session['userid']))
            return redirect(reverse('blog:index'))

    context = {}
    if 'userid' in request.session:
        context['users'] = User.objects.get(pk=request.session['userid'])
    return render(request, 'blog/create.html', context=context)

def get_post(postid, userid, check_author=True):
    post = get_object_or_404(Post, pk=postid)
    if check_author and post.user.id != userid:
        raise Http404("Post does not exist")
    return post
        

@authview.login_required
def update(request, post_id):
    post = get_post(post_id, request.session['userid'])
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            messages.add_message(request, messages.INFO, error)
        else:
            post.title = title
            post.body = body
            post.save()
            return redirect(reverse('blog:index'))
    
    context = {}
    context['post'] = post
    if 'userid' in request.session:
        context['users'] = User.objects.get(pk=request.session['userid'])
    return render(request, 'blog/update.html', context=context)

@authview.login_required
def delete(request, post_id):
    post = get_post(post_id, request.session['userid'])
    post.delete()
    return redirect(reverse('blog:index'))
