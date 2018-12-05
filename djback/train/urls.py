"train url definition"
from django.urls import path
from . import views


app_name = 'train'
urlpatterns = [
    path(r'', views.collect_data),
]
