from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post

PostLIstView = PostListView.as_view()


def post_list(request):
    qs = Post.object.all()
    q = request.Get.get()

