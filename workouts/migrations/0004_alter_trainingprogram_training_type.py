# Generated by Django 5.0.3 on 2024-04-13 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0003_trainingprogram_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingprogram',
            name='training_type',
            field=models.CharField(choices=[('Personal', 'Personal'), ('General', 'General')], max_length=10),
        ),
    ]
