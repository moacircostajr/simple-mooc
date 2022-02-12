from django.urls import path

from . import views

app_name = 'courses'  # namespace
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/detalhes', views.details, name='details'),  # https://docs.djangoproject.com/en/3.2/topics/http/urls/
]
