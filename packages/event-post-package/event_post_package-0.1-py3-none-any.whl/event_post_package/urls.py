from django.urls import path
from .views import PostListView, PostDetailView, PostEditView, PostDeleteView, ProfileView, ProfileEditView, AddLike, AddDislike, UserSearch

urlpatterns = [
    path('', PostListView.as_view(), name='post-wall'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
    path('search/', UserSearch.as_view(), name='profile-search')
]