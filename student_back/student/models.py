from django.db import models
from course.models import Department, Major, Course
from counselor.models import Counselor


# Create your models here.
class YearField(models.Field):
    def db_type(self, connection):
        return 'year'


class ClassInfo(models.Model):  # 加上Info是为了避免与关键词class冲突
    objects = models.Manager
    class_id = models.CharField(primary_key=True, max_length=10)
    class_name = models.CharField(max_length=50)
    department_id = models.ForeignKey('course.Department', on_delete=models.DO_NOTHING, db_column='department_id')
    major_id = models.ForeignKey(
        'course.Major', on_delete=models.DO_NOTHING, db_column='major_id')
    total_student = models.IntegerField(default=0)

    class Meta:
        db_table = 't_class_info'


class Student(models.Model):
    objects = models.Manager
    student_id = models.CharField(primary_key=True, max_length=12)
    student_name = models.CharField(max_length=50)
    student_gender = models.CharField(max_length=2, default='男')  # 是否可以设置check约束？
    student_nation = models.CharField(max_length=10, default='汉族')
    student_grade = YearField(default=2021)  # 注意这个year类型,字段表示学生所在年级
    department_id = models.ForeignKey(
        'course.Department', on_delete=models.DO_NOTHING, db_column='department_id')
    major_id = models.ForeignKey(
        'course.Major', on_delete=models.DO_NOTHING, db_column='major_id')
    class_id = models.ForeignKey('student.ClassInfo', on_delete=models.DO_NOTHING, db_column='class_id')
    counselor_id = models.ForeignKey('counselor.Counselor', on_delete=models.DO_NOTHING, db_column='counselor_id')
    birth_date = models.DateField(default='2021-01-01')
    length_of_schooling = models.IntegerField(default=4)
    political_status = models.CharField(max_length=20, default='群众')  # 政治面貌
    native_place = models.CharField(max_length=50, default='')  # 籍贯
    enrollment_date = models.DateField(default='2020-09-01')  # 入学日期
    dormitory_addr = models.CharField(max_length=50, default='南邮通达学生宿舍XX栋')  # 宿舍地址
    password = models.CharField(max_length=30, default=student_id)
    email = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=11, default='')
    id_number = models.CharField(max_length=18, default='')  # 身份证号码

    class Meta:
        db_table = 't_student_info'


class Score(models.Model):
    objects = models.Manager
    score_id = models.CharField(primary_key=True, max_length=20)
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING, db_column='student_id')
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING, db_column='course_id')
    course_type = models.CharField(max_length=10, default='必修')
    course_grade = models.DecimalField(max_digits=5, decimal_places=2, default=1.0)
    semester = models.IntegerField(default=1)  # 该课程考试学期，取值范围1-8
    part_time_score = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # 平时成绩
    exam_score = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # 期末成绩
    overall_score = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # 综合成绩
    get_grade = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # 所得学分
    postscript = models.CharField(max_length=20, default='')  # 备注信息：“缺考”、“缓考”、“重修”等

    class Meta:
        db_table = 't_score_info'

