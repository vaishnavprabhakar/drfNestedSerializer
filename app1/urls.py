from django.urls import path,include
from . import views

urlpatterns = [
    path('authors/', views.AuthorListCreate.as_view(), name='author'),
    
]