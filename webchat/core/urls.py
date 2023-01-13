from django.contrib.auth import views as vws
from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('login/', vws.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', vws.LogoutView.as_view(), name='logout'),
]