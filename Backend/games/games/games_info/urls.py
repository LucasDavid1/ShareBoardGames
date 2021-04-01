from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'games_info'
urlpatterns = [
    path('all/', views.retrieve_all, name='retrieve_all'),    
    path('ping/', views.ping, name='ping'),    
    path('<int:limit>/categories/', views.retrieve_categories, name='retrieve_categories'),  
    path('<int:limit>/<str:game_name>/by-name/', views.search_by_name, name='search_by_name'),    
    path('admin/', admin.site.urls),
]