from django.contrib import admin
from django.urls import path
from translator_app import views

urlpatterns = [
    path('', views.index, name='translaror_app'),
    path('translate', views.traslate, name='translaror_app'),
    

]