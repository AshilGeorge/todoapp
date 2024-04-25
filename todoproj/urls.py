"""
URL configuration for todoproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from todoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.todoView.as_view(),name="home_view"),
    path('login',views.LoginView.as_view(),name="login_view"),
    path('create',views.TodoCreateView.as_view(),name="create_todo"),
    path('detail',views.TodoList.as_view(),name="detail_todo"),
    path('delete/<int:id>',views.Delete.as_view(),name="delete_view"),
    path('edit/<int:id>',views.EditView.as_view(),name="edit_view"),

    




    

]
