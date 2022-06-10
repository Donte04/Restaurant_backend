from django.urls import path
from . import views
from knox import views as views_knox

urlpatterns = [
    path('login/', views.login),
    path('user/', views.get_user_data),
    path('register/', views.register),
    path('logout/', views_knox.LogoutView.as_view()),
    path('logouts/', views_knox.LogoutAllView.as_view())
]
