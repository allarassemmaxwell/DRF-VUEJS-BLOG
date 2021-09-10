from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
# Create your views here.




def home(request):
    return render(request, 'home.html', {})


def post_detail_view(request, post_slug=None):
    post  = get_object_or_404(Post, slug=post_slug)
    context = {'post': post}
    template = "post-detail.html"
    return render(request, template, context)


class BlogList(APIView):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()[0:4]
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    
class BlogDetail(APIView):
    def get(self, request, post_slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=post_slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)