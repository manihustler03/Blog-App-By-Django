from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create_post, name='create_post'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('post/<int:post_id>/', views.post_detail, name='post'),
    path('category-tech/', views.Category_Tech, name='category_tech'),
    path('category-cinema/', views.Category_Cinema, name='category_cinema'),
    path('category-news/', views.Category_News, name='category_news'),
    path('category-sport/', views.Category_Sport, name='category_sport'),
   
]
