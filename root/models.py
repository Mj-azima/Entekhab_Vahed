from django.db import models
#
# # Create your models here.
#
# class Class(models.Model):
#     FAVORITE_DAYS_CHOICES = [
#         ('0', 'شنبه'),
#         ('1', 'یک شنبه'),
#         ('2', 'دو شنبه'),
#         ('3', 'سه شنبه'),
#         ('4', 'چهار شنبه'),
#     ]
#     department = models.CharField(max_length=200)
#     name = models.CharField(max_length=200)
#     course_number = models.IntegerField()
#     group_number = models.IntegerField()
#     teacher =models.CharField(max_length=200)
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     first_day = models.CharField(choices=FAVORITE_DAYS_CHOICES )
#     second_day = models.CharField(choices=FAVORITE_DAYS_CHOICES , blank=True , null=True)