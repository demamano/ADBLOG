from django.urls import path
from . import views 
urlpatterns = [
    path('',views.getData),
    path('home/',views.home),
    path('<str:pk>/',views.updateData),


]