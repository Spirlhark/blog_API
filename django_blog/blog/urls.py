from django.urls import path
from .views import *

from . import views



urlpatterns = [
    path('post/', views.PostListView.as_view()),
    path('post/<int:pk>/', views.PostDetailView.as_view()),
    path('review/', views.ReviewCreateView.as_view()),
    path('post/new/', views.PostCreateView.as_view()),
    path('post/update/<int:pk>/', views.post_update),
]
