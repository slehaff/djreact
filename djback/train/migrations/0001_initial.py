# Generated by Django 2.1.2 on 2018-11-30 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageFolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingRepo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='trainingdata',
            name='repo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train.TrainingRepo'),
        ),
        migrations.AddField(
            model_name='imagefolder',
            name='train_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train.TrainingData'),
        ),
    ]
