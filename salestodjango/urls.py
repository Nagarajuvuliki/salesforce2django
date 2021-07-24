from django.contrib import admin
from django.urls import path
from salestodjango import views

urlpatterns = [
    path("",views.index,name="index"),
    #path("1",views.Insertusers)
]