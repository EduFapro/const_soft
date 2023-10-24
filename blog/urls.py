from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartingPageAPIView.as_view(), name="starting-page"),
    path("posts", views.AllPostsAPIView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.SinglePostAPIView.as_view(),
         name="post-detail-page"),  # /posts/my-first-post
]
