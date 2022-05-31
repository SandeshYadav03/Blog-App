from django.contrib import admin
from django.urls import path
from . import views


app_name = 'app'
    
urlpatterns = [
    path('', views.homepage, name= "homepage"),
    path('login/', views.login_user, name="login_user"),
    path('logout/', views.logout_user, name="logout_user"),
    path('signup/', views.signup, name="signup"),
    path('contact_user/', views.contact_user, name="contact_user"),
    path('<id>/', views.single_post, name= "single_post"),
    path('add_comment/<post_id>', views.add_comment, name="add_comment"),   
    path('about', views.about_user, name="about_user"),
]
