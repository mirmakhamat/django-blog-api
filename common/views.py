from .serializers import (
    CategorySerializer,
    AllArticlesSerializer,
    UserSerializer,
    TagSerializer,
    FAQSerializer,
    ArticleSerializer)

from rest_framework import generics
from .models import Category, Article, User, Tag, FAQ

from datetime import timedelta
from django.utils.timezone import now


class FAQListView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = AllArticlesSerializer


class ArticleByTagListView(generics.ListAPIView):
    serializer_class = AllArticlesSerializer

    def get_queryset(self):
        tag_id = self.kwargs.get('pk')
        return Article.objects.filter(tag__id=tag_id)


class ArticleByCategoryListView(generics.ListAPIView):
    serializer_class = AllArticlesSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('pk')
        return Article.objects.filter(category__id=category_id)


class ArticleByAuthorListView(generics.ListAPIView):
    serializer_class = AllArticlesSerializer

    def get_queryset(self):
        author_id = self.kwargs.get('pk')
        return Article.objects.filter(author__id=author_id)


class ArticleTodayListView(generics.ListAPIView):
    queryset = Article.objects.filter(
        created_at__gte=now() - timedelta(hours=24))
    serializer_class = AllArticlesSerializer


class ArticlePopularListView(generics.ListAPIView):
    queryset = Article.objects.all().order_by('-view_count')
    serializer_class = AllArticlesSerializer


class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view_count += 1
        instance.save()

        return self.retrieve(request, *args, **kwargs)
