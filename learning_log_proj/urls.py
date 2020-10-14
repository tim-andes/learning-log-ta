"""learning_log_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# 1.
from django.contrib import admin
from django.urls import path, include
# 2.
urlpatterns = [
    path('admin/', admin.site.urls), # 3.
    path('users/', include('users.urls')),
    path('', include('learning_logs.urls')),
]

## 1. These two import lines import a model and function to manage URLs

## 2. The body defines the urlpatterns available
## In this urls.py file, which represents the project as a whole, the urlpatterns
## variable includes sets of URLs from the apps in the project.

## 3. This code includes the module admin.site.urls , which defines all the
# URLs that can be requested from the admin site.

## 4. We’ve added a line to include the module learning_logs.urls
