from django.urls import path

from .views import HomePageView,AboutPageView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView

urlpatterns = [
    path('',HomePageView.as_view(),name='Home'),
    path('about/',AboutPageView.as_view(),name='About'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post_detail'),
    path('post/new/',PostCreateView.as_view(),name='post_new'),
    path('post/<int:pk>/edit/',PostUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post_delete'),
]