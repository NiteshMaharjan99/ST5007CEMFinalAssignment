from django.urls import URLPattern, path
from account import views

urlpatterns = [
    path('userLogin', views.userLogin, name='userLogin'),
    path('userRegister', views.userRegister, name='userRegister'),
    path('logout', views.logout, name='logout'),

]