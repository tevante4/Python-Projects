# Generated by Django 3.2.6 on 2022-06-04 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0006_auto_20210831_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangoclasses',
            name='duration_in_min',
            field=models.FloatField(choices=[(180.0, 180.0), (45.0, 45.0), (90.0, 90.0)], default=45),
        ),
        migrations.AlterField(
            model_name='djangoclasses',
            name='title',
            field=models.CharField(choices=[('Physical Education', 'Physical Education'), ('Math', 'Math'), ('Business', 'Business'), ('Visual Arts', 'Visual Arts'), ('Performing Arts', 'Performing Arts'), ('Computer Science', 'Computer Science'), ('Consumer Science', 'Consumer Science'), ('Social Studies', 'Social Studies'), ('English', 'English'), ('Science', 'Science'), ('Foreign Language', 'Foreign Language')], max_length=60),
        ),
    ]
