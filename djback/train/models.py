"Tralining data repository"
from django.db import models


class TrainingRepo(models.Model):
    name = models.CharField(max_legth=30)
    started = models.DateField


class TrainingData(models.Model):
    repo = models.ForeignKey(TrainingRepo, on_delete=models.CASCADE)
    width = models.PositiveIntegerField
    height = models.PositiveIntegerField
