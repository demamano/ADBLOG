# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article,Reporter
from .serializers import ArticleSerializer
@api_view(['GET'])
def getData(request):
    items = Article.objects.all()
    serializer = ArticleSerializer(items,many=True)
    return Response(serializer.data)




