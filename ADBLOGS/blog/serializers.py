from rest_framework import serializers
from .models import Article,Reporter
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        