from django.db import models
from course.models import Department

# Create your models here.


class Counselor(models.Model):
    objects = models.Manager
    counselor_id = models.CharField(primary_key=True, max_length=8)
    counselor_name = models.CharField(max_length=50)
    department_id = models.ForeignKey(Department, on_delete=models.DO_NOTHING, db_column='department_id')
    counselor_gender = models.CharField(max_length=2, default='男')
    counselor_nation = models.CharField(max_length=10, default='汉族')
    phone = models.CharField(max_length=11, default='')
    email = models.CharField(max_length=50, default='')
    password = models.CharField(max_length=30, default=counselor_id)

    class Meta:
        db_table = 't_counselor_info'
