from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
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
    return HttpResponse("")

def get_post(postid, userid, check_author=True):
    post = get_object_or_404(Post, pk=postid)
    if check_author and post.user.id != userid:
        raise Http404("Post does not exist")
    return post
        

@authview.login_required
def update(request, post_id):
    return HttpResponse("")

@authview.login_required
def delete(request, post_id):
    return HttpResponse("")
