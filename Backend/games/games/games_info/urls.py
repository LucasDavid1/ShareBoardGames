from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'games_info'
urlpatterns = [
    path('<int:limit>/all/', views.retrieve_all, name='retrieve_all'),    
    path('admin/', admin.site.urls),
]