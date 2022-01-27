from rest_framework import generics
from rest_framework.response import Response
from .models import Post
from rest_framework.decorators import api_view
from .serializers import PostListSerializer, PostDetailSerializer, ReviewCreateSerializer, PostCreateSerializer, PostUpdateSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .service import PostFilter


class PostListView(generics.ListAPIView):
    """Вывод списка постов"""
    serializer_class = PostListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PostFilter

    def get_queryset(self):
        posts = Post.objects.filter(draft=False)
        return posts


class PostDetailView(generics.RetrieveAPIView):
    """Вывод поста"""

    queryset = Post.objects.filter(draft=False)
    serializer_class = PostDetailSerializer


class ReviewCreateView(generics.CreateAPIView):
    """Добавление отзыва к посту"""

    serializer_class = ReviewCreateSerializer


class PostCreateView(generics.CreateAPIView):
    """Добавление поста"""

    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@api_view(['GET', 'PUT', 'DELETE'])
def post_update(request, pk):
    """Изменение поста"""
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNoteExist:
        return Response(status=404)
    if request.method == 'GET':
        serializer = PostUpdateSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        print(111)
        serializer = PostUpdateSerializer(post, data=request.data)
        print(serializer)
        if serializer.is_valid():
            print(333)
            serializer.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=204)
