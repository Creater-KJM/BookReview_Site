from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request,'home.html', { 'posts' : posts })

def write(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        post = form.save(commit=False)
        form.save()
        return redirect('review',post_pk = post.pk)
    else:
        form = PostForm()
    return render(request,'write.html',{ 'form' : form })

def review(request, post_pk):
    post = Post.objects.get(pk = post_pk)
    return render(request,'review.html', { 'post' : post })

def modify(request,post_pk):
    post = Post.objects.get(pk = post_pk)
    if request.method == 'POST':
        form = PostForm(request.POST,instance = post)
        post = form.save(commit = False)
        form.save()
        return redirect('review', post.pk)
    else:
        form= PostForm(instance = post)
    return render(request,'modify.html',{'form':form})

def delete(request,post_pk):
    post= Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('home')

