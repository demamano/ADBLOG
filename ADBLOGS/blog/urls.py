from django.urls import path
from . import views 
urlpatterns = [
    path('',views.getData),
    path('home/',views.home, name='blog-home'),
    # path('login/',views.login),
    path('<str:pk>/',views.updateData),
    



]