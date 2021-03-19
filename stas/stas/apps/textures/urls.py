from django.urls import path

from . import views

app_name = 'textures'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:texture_id>/', views.detail, name='detail'),

]
