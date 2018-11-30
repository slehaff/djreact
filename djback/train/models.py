"Tralining data repository"
from django.db import models


class TrainingRepo(models.Model):
    "Training data repository"
    name = models.CharField(max_length=30)
    started = models.DateField


class TrainingData(models.Model):
    "Training data set comprising train, test and validate data"
    repo = models.ForeignKey(TrainingRepo, on_delete=models.CASCADE)
    width = models.PositiveIntegerField
    height = models.PositiveIntegerField


class ImageFolder(models.Model):
    "Single image folder containing input and ground truth image"
    train_data = models.ForeignKey(TrainingData, on_delete=models.CASCADE)
