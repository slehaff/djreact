"Adding train models to the admin view! "
from django.contrib import admin
from .models import *


admin.site.register(TrainingData)
admin.site.register(TrainingRepo)
admin.site.register(ImageFolder)

# Register your models here.
