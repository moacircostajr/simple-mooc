from django.urls import path

from . import views

app_name = 'core'  # namespace
urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contact, name='contact'),
]
