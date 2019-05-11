from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="photo-home"),
    path('about/',views.about, name="photo-about"),
]