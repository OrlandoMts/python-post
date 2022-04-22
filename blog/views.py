from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, UpdateView, DeleteView
from .forms import PostCreateForm
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class BlogListView(View):
    
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'blog/list_post.html', context)


class BlogCreateView(View):
    
    def get(self, request, *args, **kwargs):
        form = PostCreateForm()
        context = {
            'form': form,
        }
        return render(request, 'blog/post_create.html', context)
        
    # Asi registro un nuevo post en la bd
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = PostCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')

                p, created = Post.objects.get_or_create(title=title, content=content)
                p.save()

                return redirect('blog:home')

        
        context = {}
        return render(request, 'blog/post_create.html', context)


class BlogDetailView(View):

    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        context = {
            'post': post
        }

        return render(request, 'blog/post_detail.html', context)


class BlogUpdateView(UpdateView):
    
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_update.html'

    def get_success_url(self) -> str:
        pk = self.kwargs['pk']
        return reverse_lazy('blog:detail', kwargs={'pk':pk})


class BlogDeleteView(DeleteView):

    model = Post
    fields = '__all__'
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog:home')