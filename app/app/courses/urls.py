from django.urls import path

from . import views

app_name = 'courses'  # namespace
urlpatterns = [
    path('', views.index, name='index'),
]
