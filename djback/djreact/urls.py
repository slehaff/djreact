"""djreact URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('djreact/', views.index),
    path('admin/', admin.site.urls),
    # path('djapi/v1/', include('djapi.urls')),
    # path('resnet/v1/', include('resnet.urls')),
    path('train', include('train.urls')),
]
