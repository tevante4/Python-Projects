from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

Class_Title = {
    ('Business', 'Business'),
    ('Computer Science', 'Computer Science'),
    ('Consumer Science', 'Consumer Science'),
    ('English', 'English'),
    ('Foreign Language', 'Foreign Language'),
    ('Math', 'Math'),
    ('Performing Arts', 'Performing Arts'),
    ('Physical Education', 'Physical Education'),
    ('Science', 'Science'),
    ('Social Studies', 'Social Studies'),
    ('Visual Arts', 'Visual Arts'),
}

Class_Duration = {
    (45.00, 45.00),
    (90.00, 90.00),
    (180.00, 180.00),
}

class djangoClasses(models.Model):
    title = models.CharField(max_length=60, choices=Class_Title)
    course_number = models.SmallIntegerField(unique=True, blank=False, null=False, default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    instructor_name = models.CharField(max_length=60, default="", blank=True, null=False)
    duration_in_min = models.FloatField(default=45, choices=Class_Duration)

    objects = models.Manager()

    def __str__(self):
        return self.title

