from rest_framework.authtoken.views import  obtain_auth_token
from django.contrib import admin
from django.urls import path
from main.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Todolist/',TodoList.as_view()),
    path('tokenget/',obtain_auth_token),
    path('todoget/<int:pk>/',Todoget.as_view()),
    path('deletetodo/<int:pk>/',TodoList.as_view()),
]
