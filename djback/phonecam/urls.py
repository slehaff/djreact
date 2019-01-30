"phonecam url definition"
from django.urls import path
from . import views


app_name = 'phonecam'
urlpatterns = [
    path(r'', views.camera),
]
