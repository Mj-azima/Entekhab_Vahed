from django.db import models

# Create your models here.

class Pic(models.Model):
    name = models.ForeignKey()
    image = models.ImageField(_('person image'), upload_to='db/images/%Y/%m/%d/', height_field=None, width_field=None,max_length=200)

DAY_CHOICES = [
    (0, 'Saturday'),
    (1, 'Sunday'),
    (2, 'Monday'),
    (3, 'Tuesday'),
    (4, 'Wednesday'),
]

class Course(models.Model):
    department = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    course_number = models.IntegerField()
    group_number = models.IntegerField()
    teacher = models.CharField(max_length=120)
    start_time = models.CharField(max_length=120)
    end_time = models.CharField(max_length=120)
    first_day = models.IntegerField(choices=DAY_CHOICES)
    second_day = models.IntegerField(choices=DAY_CHOICES)
