from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import CustomLoginView
from django.views.generic import TemplateView

app_name = 'accounts'

urlpatterns = [
    path('signup/',
        views.SignUpView.as_view(),
        name='signup'),

    path('signup_success/',
        views.SignUpSuccessView.as_view(),
        name='signup_success'),

    path('login/',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login'),

    path('logout/',
        auth_views.LogoutView.as_view(template_name='logout.html'),
        name='logout'),

    path('login/', CustomLoginView.as_view(), name='login'),

    path('login_success/', TemplateView.as_view(template_name='login_success.html'), name='login_success'),
]