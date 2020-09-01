from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login, name='users/login'),
    path('signup/', views.signup, name='users/signup'),
    path('logout/', views.logout, name='users/logout'),
]
