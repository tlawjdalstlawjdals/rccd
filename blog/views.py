from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
#
from django.contrib.auth.decorators import login_required
#
from django.views.generic import TemplateView

from django.conf import settings
from django.core.files.storage import FileSystemStorage

import matlab.engine

# from .MatlabShell import MatlabShell
# import matlab.engine

#main page (list)
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

#list -> detail
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
#
@login_required
#
#new post
def post_new(request):
    if request.method == "POST":
        # form = PostForm(request.POST)
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()

            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()


    return render(request, 'blog/post_edit.html', {'form': form})

#
@login_required
#
#edit post
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        # form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

#image post_spect(decay correction)
# def post_decay(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})
# def post_decay(request):
#     # posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
#     # return render(request, 'blog/post_decay.html', {'posts': posts})
#     return render(request, 'blog/post_decay.html')


def post_decay(request):
    if request.method == 'POST' and request.FILES['myfile']:
        engine = matlab.engine.start_matlab()
        # base = 'Decay_run_ver2'
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        # getattr(engine, 'matlab.engine.shareEngine')(base, nargout=0)
        # matlab start
        # engine = matlab.engine.start_matlab()
        # base = 'Decay_run_ver2'
        # P = uploaded_file_url

        # getattr(engine, 'run')(base, nargout=0)
        # matlab end
        engine.Decay_run_ver2(nargout=0)
        return render(request, 'blog/post_decay.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'blog/post_decay.html')

#
@login_required
#
#draft_list
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

#
@login_required
#
#draft_list -> publish
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

#
@login_required
#
#draft_list -> remove
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


# #
# @login_required
# #
# def post_spect(request, pk):
#     eng = matlab.engine.start_matlab()
#
#     post = get_object_or_404(Post, pk=pk)
#     post.publish()
#     return redirect('post_detail', pk=pk)
#
