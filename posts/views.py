from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer

class PostList(ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    # permission_classes = (permissions.IsAdminUser,) # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

class PostDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAdminUser,) # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer



