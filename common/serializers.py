from rest_framework import serializers
from .models import Article, Category, User, Tag, FAQ


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AllArticlesSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    author = UserSerializer()

    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'author',
            'image',
            'description',
            'category',
            'created_at',
        )


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    author = UserSerializer()
    tag = TagSerializer(many=True)
    class Meta:
        model = Article
        fields = '__all__'