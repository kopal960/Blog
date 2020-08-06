from django.shortcuts import render,redirect ,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.views.generic import DetailView,UpdateView, DeleteView, ListView
from .forms import CreatePost
from .models import Post
from django.db.models import Q 

def about(request):
    context = { 
        'page' : 2
    }
    return render(request , 'blog/About.html',context)
@login_required
def newpost(request):
    if request.method == 'POST':
        form = CreatePost(request.POST)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            messages.success(request, f"Your post,{form.instance.title} has been created")
            return redirect(form.instance.get_absolute_url())
    else:
        form = CreatePost()
    context = { 'form':form }
    return render (request, "blog/post_form.html" , context)
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 5
    query=''
    def get_queryset(self,*args,**kwargs):
        post_filtered = Post.objects.filter(Q(title__icontains=self.query) |Q(author__username__icontains=self.query) )
        ordering = ['-date_posted']
        return post_filtered.order_by('-date_posted')
    def get(self, request):
        if request.GET.get('query'):
            self.query = request.GET.get('query')
        return super().get(request)

class UserPostListView(ListView):
    model = Post
    context_object_name = 'userposts'
    paginate_by = 5
    def get_context_data(self, **kwargs):          
        context = super().get_context_data(**kwargs)                     
        posts_author = self.kwargs.get('usernam')
        context["posts_author"] = posts_author
        return context
    def get_queryset(self,*args,**kwargs):
        curUser = get_object_or_404(User , username = self.kwargs.get('usernam'))
        ordering = ['-date_posted']
        query = ''
        if self.kwargs.get('query'):
            query = self.kwargs.get('query')
        return Post.objects.filter(author =curUser)
class PostDetailView(DetailView):
    model = Post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Post
    fields = ['title','date_posted','description','content' ]
    template_name = 'blog/post_form.html'
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = Post
    success_url = "/"
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False