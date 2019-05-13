from django.shortcuts import render
from django.http import HttpResponse
from .models import Post   # to get real data from model
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin       # So that user can not directly access the create blog page without login
#Load dummy data
# posts = [
#     {
#         'author':"thebadcoder",
#         'title':"django learning",
#         'content':'First post by tbc',
#         'date_posted':'August 27,2018'
#     },
#     {
#         'author':"the python",
#         'title':"data processing learning",
#         'content':'Latest post by the python',
#         'date_posted':'Jan 27,2018'
#     }
# ]

# Create your views here.
def home(request):
    # Real data
    posts = Post.objects.all()      # Get all posts
    context ={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

# Replace function based views with the class based views which have cool functionality than the function based ones.
# ListView,DetailsView,CreateView
class PostListView(ListView):   # This also affects url in original app
    model = Post
    #<app>/<model>_<viewtype>.html 
    template_name = 'blog/home.html'    # custom page redirection
    context_object_name = 'posts'       # view needs an object to work on
    ordering = ['-date_posted']

# Detail view
class PostDetailView(DetailView):   # This also affects url in original app
    model = Post

# Create view
class PostCreateView(LoginRequiredMixin, CreateView):   # This also affects url in original app
    model = Post
    fields = ['title','content']
    # Need author context to create post or error will be thown
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)     #explicitely calling is valid method of super class

    # Redirection should be done explicitely after creation of blog

#update view
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):   # This also affects url in original app
    model = Post
    fields = ['title','content']
    # Need author context to create post or error will be thown
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)     #explicitely calling is valid method of super class
    
    # To regualte users to be able to update their own posts
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# Delete view
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):   # This also affects url in original app
    model = Post
    success_url = '/'
    # To regualte users to be able to update their own posts
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

def about(request):
    return render(request,'blog/about.html',{'title':'About'})