
from django.contrib import admin
from django.urls import path
from posts import views
from users import views as views_users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', views.list_posts, name='Post'),
    path('Sign/', views_users.view_login, name='Login'),
    path('Logout/', views_users.view_logout, name='Logout'),
    path('SignUp/', views_users.view_sing_up, name='SignUp')

]
