from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail, PostListSearch, PostCreate, PostUpdate, PostDelete, CategiryListView

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(),name='post_detail'),
    path('search/', PostListSearch.as_view()),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('categories/<int:pk>', CategiryListView.as_view(), name='category_list'),
]