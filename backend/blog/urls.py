from django.urls import path

from .views import ArticleListCreateAPIView, ArticleRetrieveUpdateDestroyAPIView, CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('/', ArticleListCreateAPIView.as_view(), name='article-list-create'),
    path('/<int:id>/', ArticleRetrieveUpdateDestroyAPIView.as_view(), name='article-retrieve-update-destroy'),
    path('/categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('/categories/<int:id>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy'),
]