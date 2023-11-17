from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.CategoryListView.as_view(), name="category"),
    path('article/', views.ArticleListView.as_view(), name="article"),
    path('article/tag/<int:pk>', views.ArticleByTagListView.as_view(), name="article-by-tag"),
    path('article/category/<int:pk>', views.ArticleByCategoryListView.as_view(), name="article-by-category"),
    path('article/author/<int:pk>', views.ArticleByAuthorListView.as_view(), name="article-by-author"),
    path('article/popular/', views.ArticlePopularListView.as_view(), name="article-popular"),
    path('article/today/', views.ArticleTodayListView.as_view(), name="article-today"),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name="article-detail"),
    path('author/', views.UserListView.as_view(), name="author"),
    path('tag/', views.TagListView.as_view(), name="tag"),
    path('faq/', views.FAQListView.as_view(), name="faq"),
]
