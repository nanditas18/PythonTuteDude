from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination

from .models import Post
from .serializers import PostSerializer

class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello world using REST API's"})

class PostPagination(PageNumberPagination):
    page_size = 5  # Limits list returns to 5 items per page
    page_size_query_param = 'page_size'
    max_page_size = 100

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination

 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = {
        'author__username': ['exact'],
        'created_at': ['exact', 'gte', 'lte'], 
    }
    
    search_fields = ['title', 'content']
    
    ordering_fields = ['created_at', 'title']
    ordering = ['-created_at'] 
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]