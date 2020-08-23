from django.shortcuts import render,redirect ,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.views.generic import DetailView,UpdateView, DeleteView, ListView 
from django.views.generic.base import RedirectView
from .forms import CreatePost,CreateComment
from .models import Post ,Comment,Vote
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
    ordering = '-date_posted' ,'-id'
    paginate_by = 5
    def get_context_data(self, **kwargs):          
        context = super().get_context_data(**kwargs)                     
        context['page'] = 1
        context['base_url'] = '?'
        return context
    def get(self, request):
        return super().get(request)

class UserPostListView(PostListView):
    context_object_name = 'userposts'
    def get_queryset(self,*args,**kwargs):
        curUser = get_object_or_404(User , username = self.kwargs.get('username'))
        query_set = super().get_queryset(*args , **kwargs)
        return query_set.filter(author =curUser)
    def get(self, request,username):
        return super().get(request)

class PostSearchView(PostListView):
    query = ''
    def get_queryset(self,*args,**kwargs): 
        return super().get_queryset(*args ,**kwargs).filter( Q(title__icontains= self.query)|Q(author__username__icontains= self.query) )
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['base_url'] = '/search/?query'+'=' +self.query + "&"
        return context
    def get(self,request): 
        self.query = request.GET.get('query')
        return super().get(request)
@login_required        
def upvote(request,pk):
    post = get_object_or_404(Post ,pk = pk)
    vote = get_object_or_404(Vote , post = post, user= request.user)
    vote.Like = not vote.Like
    vote.save()
    return redirect("post-detail" , pk )

class PostDetailView(DetailView):
    model = Post
    context = {}
    def get_context_data(self, **kwargs):
        post = get_object_or_404(Post , pk = self.kwargs.get('pk'))
        ordering = ['-date_posted']
        comments = Comment.objects.filter(post= post).filter( active=True ).order_by('-dated' ,'-id')
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = CreateComment()
        context['comments'] = comments
        context['Upvotes'] = post.vote_set.filter(Like=True).count()
        return context
    def post(self, request, pk):
       post = get_object_or_404(Post, pk=pk)
       form = CreateComment(request.POST)
       if form.is_valid():
           form.instance.post = post
           form.instance.name = request.user
           form.save()
           return redirect('post-detail', post.pk) 

class CPostDetailView(LoginRequiredMixin ,PostDetailView):
    pass

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