from django.db import models


# Create your models here.
class Department(models.Model):
    objects = models.Manager
    department_id = models.CharField(primary_key=True, max_length=2)
    department_name = models.CharField(max_length=50)

    # 更改数据库表名字
    class Meta:
        db_table = 't_department_info'


class Major(models.Model):
    objects = models.Manager
    major_id = models.CharField(primary_key=True, max_length=4)
    major_name = models.CharField(max_length=50)
    department_id = models.ForeignKey(Department, on_delete=models.DO_NOTHING, db_column='department_id')
    required_grade = models.DecimalField(max_digits=5, decimal_places=2, default=80)
    elective_grade = models.DecimalField(max_digits=5, decimal_places=2, default=20)

    class Meta:
        db_table = 't_major_info'


class Course(models.Model):
    objects = models.Manager
    course_id = models.CharField(primary_key=True, max_length=8)
    course_name = models.CharField(max_length=50)
    department_id = models.ForeignKey(Department, on_delete=models.DO_NOTHING, db_column='department_id')
    major_id = models.ForeignKey(Major, on_delete=models.DO_NOTHING, db_column='major_id')
    teacher_name = models.CharField(max_length=50, default='')
    course_duration = models.IntegerField(default=32)  # 授课时长，单位'h'
    course_grade = models.DecimalField(max_digits=5, decimal_places=2, default=1.0)  # 课程学分
    course_type = models.CharField(max_length=10, default='必修')  # 课程类型：“选修”或者“必修”

    class Meta:
        db_table = 't_course_info'
