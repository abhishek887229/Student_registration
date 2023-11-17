from django.contrib import admin
from django.urls import path
from . import views

app_name="shop"

urlpatterns = [
    path("",views.show_product),
    path("item/<int:id>",views.detail,name="detail_view"),
]
