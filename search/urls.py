from django.contrib import admin
from django.urls import path,include
from search import views
urlpatterns = [
    path('',views.index,name="index"),
    path('search/',views.search,name="search")

]
