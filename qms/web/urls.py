from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index,name = "home"),
    path('privacy/', views.privacy,name = "privacy"),
    path('signin', views.signin,name = "signin"),
    path('signup', views.signup,name = "signup"),
]