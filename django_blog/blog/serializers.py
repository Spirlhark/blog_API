from rest_framework import serializers
from .models import *


# class PostSerializer(serializers.Serializer):
#
#     class Meta:
#         model = Post
#         fields = '__all__'
#
#     def create(self, validated_data):
#         return Post.objects.create(**validated_data)
#         print(222)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.title)
#         instance.save()
#         print(111)
#         return instance


class FilterReviewListSerializer(serializers.ListSerializer):
    """Фильтрациа отзывов, только parents"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Вывод отзыва рекурсивно"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class PostListSerializer(serializers.ModelSerializer):
    """Список постов"""
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'author')


class PostCreateSerializer(serializers.ModelSerializer):
    """Добавление поста"""
    author = serializers.SerializerMethodField(read_only=True)

    def get_author(self, obj):
        return str(obj.author.id)

    class Meta:
        model = Post
        fields = '__all__'


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""

    class Meta:
        model = Review
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    """Вывод отзыва"""
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = ("name", "text", "children")


class PostDetailSerializer(serializers.ModelSerializer):
    """Описание поста"""
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Post
        exclude = ('draft', )
        # fields = '__all__'


class PostUpdateSerializer(serializers.ModelSerializer):
    """Обновление поста"""
    class Meta:
        model = Post
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
