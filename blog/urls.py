from django.urls import path
from . import views
from .views import ( PostDetailView,
                    PostUpdateView, 
                    PostDeleteView,
                    PostListView,
                    UserPostListView,
                    CPostDetailView
                    )
urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('about/',views.about, name="blog-about"),
    path('post/user/<str:username>/',UserPostListView.as_view() ,name ="user-posts"),
    path("post/post_form/", views.newpost , name="newpost"),
    path("post/afterlogin/<int:pk>", CPostDetailView.as_view() ,name="cpost-detail"),
    path("post/<int:pk>",PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/",PostUpdateView.as_view(),name="post-update"),
    path("post/<int:pk>/delete/",PostDeleteView.as_view(),name="post-delete"),
]