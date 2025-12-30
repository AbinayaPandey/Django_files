from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", views.MyFunction, name="home"),
    path("aic/", views.AliceInChains, name="alice_in_chains"),
]
