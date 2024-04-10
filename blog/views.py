from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm

def blog_list(request):
    posts = Blog.objects.all().order_by('-published_date')
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/blog_detail.html', {'post': post})

@login_required # type: ignore
def blog_edit(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', pk=post.pk)
    else:
        form = BlogForm(instance=post)
    return render(request, 'blog/blog_edit.html', {'form': form})
