from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer
@api_view(['GET'])
def getData(request):
    items = Article.objects.all()
    serializer = ArticleSerializer(items,many=True)
    return Response(serializer.data)
@api_view(['PUT'])
def updateData(request,pk):
    item = Article.objects.get(id=pk)
    serializer = ArticleSerializer(item,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['POST'])
def create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['GET'])
def home(request):
    context = {
        'posts': Article.objects.all()
    }
    return render(request,'blog/index.html',context)




