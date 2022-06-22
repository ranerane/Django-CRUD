from django.views import generic
from I4G001574BEC.blog.models import Post
from django.urls import reverse_lazy

# Create your views here.
class PostListView(generic.ListView):
    model = Post

class PostCreateView(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

class PostUpdateView(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

class PostDeleteView(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")







 