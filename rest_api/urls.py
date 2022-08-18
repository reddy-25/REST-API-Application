"""rest_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
import user.views as views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.api import RegisterApi

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('user/', include('user.urls')),
    path('user/register/', RegisterApi.as_view()),
    path('user/login/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
    path('advisor/', views.addadvisor.as_view()),
    path('user/<int:pk>/advisor/', views.get_advisors.as_view()),
    path('user/<int:pk>/advisor/<int:id>/', views.add_booking.as_view()),
    path('user/<int:id>/advisor/booking/', views.get_booking.as_view())
]

