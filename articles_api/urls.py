from django.urls import path
from articles_api import views

urlpatterns = [
    path('article/create/', views.create_article, name="article-create"),
    path('article/list/', views.fetch_articles, name="article-list"),
    path('article/update/<int:id>/', views.update_article, name="update-article"),
    path('article/detail/<int:id>/', views.fetch_article, name="article-detail"),
    path('article/delete/<int:id>/', views.delete_article, name="delete-article"),
]
