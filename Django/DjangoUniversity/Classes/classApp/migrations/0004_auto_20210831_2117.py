# Generated by Django 3.2.6 on 2022-06-04 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0003_auto_20210831_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangoclasses',
            name='duration_in_min',
            field=models.FloatField(choices=[('90', 90), ('45', 45), ('180', 180)], default=45),
        ),
        migrations.AlterField(
            model_name='djangoclasses',
            name='title',
            field=models.CharField(choices=[('Foreign Language', 'Foreign Language'), ('Physical Education', 'Physical Education'), ('Business', 'Business'), ('Social Studies', 'Social Studies'), ('Performing Arts', 'Performing Arts'), ('Computer Science', 'Computer Science'), ('English', 'English'), ('Science', 'Science'), ('Visual Arts', 'Visual Arts'), ('Math', 'Math'), ('Consumer Science', 'Consumer Science')], max_length=60),
        ),
    ]
