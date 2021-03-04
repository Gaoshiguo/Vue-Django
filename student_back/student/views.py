import json
from re import T
from django.db.models.fields import DateField
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Score, Student, ClassInfo
from counselor.models import Counselor
from course.models import Department, Major
from course.views import get_current_student_is_failed
from pyecharts.charts import Bar, Line, Timeline, Pie
from pyecharts import options as opt
from pyecharts.globals import ThemeType, ChartType, SymbolType

# Create your views here.


def get_line(x, y, y_name,x_name):
    print(y_name)
    new_bar = (
        Bar()
        .add_xaxis(x)
    )
    for y_label in y:
        new_bar.add_yaxis(
            y_label,
            y[y_label],
            color="#409EFF",
            label_opts=opt.LabelOpts(),
            # is_smooth=True,
            markline_opts=opt.MarkLineOpts(
                data=[opt.MarkLineItem(type_="average")]),
            markpoint_opts=opt.MarkPointOpts(
                data=[opt.MarkPointItem(type_='max', name="最大值")])
        )
    new_bar.set_series_opts(areastyle_opts=opt.AreaStyleOpts(
        opacity=0.5), label_opts=opt.LabelOpts(is_show=False))
    new_bar.set_global_opts(
        datazoom_opts=opt.DataZoomOpts(type_='inside'),
        legend_opts=opt.LegendOpts(is_show=True),
        yaxis_opts=opt.AxisOpts(name=y_name, name_textstyle_opts=opt.TextStyleOpts(
            color="black")),
        xaxis_opts=opt.AxisOpts(
            name=x_name, name_textstyle_opts=opt.TextStyleOpts(color="black"), type_="category",
            )),
    return new_bar.dump_options_with_quotes()

def index(request):
    return HttpResponse('This is the student index')

# 返回所有用户数据
def get_all_student_information(request):
    if request.method == "GET":
        all_students_information = {
            "has_data": False,
            "data_list": []
        }
        # 获取所有学生
        all_students_obj = Student.objects.filter().all()

        department_data = Department.objects.filter().all()
        department_dict = {}
        for data in department_data:
            department_dict[str(data.department_id)] = data.department_name

        major_data = Major.objects.filter().all()
        major_dict = {}
        for data in major_data:
            major_dict[str(data.major_id)] = data.major_name

        counselor_data = Counselor.objects.filter().all()
        counselor_dict = {}
        for data in counselor_data:
            counselor_dict[str(data.counselor_id)] = data.counselor_name

        class_data = ClassInfo.objects.filter().all()
        class_dict = {}
        for data in class_data:
            class_dict[str(data.class_id)] = data.class_name

        all_students_information['has_data'] = True
        for stu_obj in all_students_obj:
            temp_data = {
                "student_id": stu_obj.student_id,
                "student_name": stu_obj.student_name,
                "student_grade": stu_obj.student_grade,
                "department_id": stu_obj.department_id.department_id,
                "department_name": department_dict[str(stu_obj.department_id.department_id)],
                "class_id": stu_obj.class_id.class_id,
                "class_name": class_dict[str(stu_obj.class_id.class_id)],
                "major_id": stu_obj.major_id.major_id,
                "major_name": major_dict[str(stu_obj.major_id.major_id)],
                "counselor_id": stu_obj.counselor_id.counselor_id,
                "counselor_name": counselor_dict[str(stu_obj.counselor_id.counselor_id)],
                "is_failed": get_current_student_is_failed(stu_obj.student_id) if get_current_student_is_failed(stu_obj.student_id) == "是" else "否"
            }
            all_students_information['data_list'].append(temp_data)
        return JsonResponse(all_students_information, safe=False)
    else:
        return HttpResponse("Error")


# 获取单个学生的详细信息
def get_current_detail_student(request):
    if request.method == "GET":
        current_student_id = request.GET.get("student_id")
        student_detail = Student.objects.filter(
            student_id=current_student_id)[0]
        if student_detail:
            current_student_info = {
                "has_data": True,
                "data_list": {
                    "学号": student_detail.student_id,
                    "姓名": student_detail.student_name,
                    "年级": student_detail.student_grade,
                    "民族": student_detail.student_nation,
                    "院系编号": Department.objects.filter(department_id=student_detail.department_id.department_id
                                                      )[0].department_id,
                    "院系": Department.objects.filter(department_id=student_detail.department_id.department_id
                                                    )[0].department_name,
                    "专业编号": Major.objects.filter(major_id=student_detail.major_id.major_id)[0].major_id,
                    "专业": Major.objects.filter(major_id=student_detail.major_id.major_id)[0].major_name,
                    "班级编号": ClassInfo.objects.filter(class_id=student_detail.class_id.class_id)[0].class_id,
                    "班级": ClassInfo.objects.filter(class_id=student_detail.class_id.class_id)[0].class_name,
                    "辅导员编号": Counselor.objects.filter(counselor_id=student_detail.counselor_id.counselor_id
                                                      )[0].counselor_id,
                    "辅导员": Counselor.objects.filter(counselor_id=student_detail.counselor_id.counselor_id
                                                    )[0].counselor_name,

                    "出生日期": student_detail.birth_date,
                    "学制": student_detail.length_of_schooling,
                    "政治面貌": student_detail.political_status,
                    "生源地": student_detail.native_place,
                    "入学日期": student_detail.enrollment_date,
                    "宿舍地址": student_detail.dormitory_addr,
                    "电子邮箱": student_detail.email,
                    "联系电话": student_detail.phone,
                    "身份证号码": student_detail.id_number,
                },
            }
        else:
            current_student_info = {
                "has_data": False,
                "data_list": {},
            }
        print("当前学生ID:", current_student_id)
        return JsonResponse(current_student_info, safe=False)
    else:
        return HttpResponse("Error")


def get_student_score_chart(request):
    print("打印请求")
    if request.method == "GET":
        temp_result = {
            "has_data": False
        }
        kw = {}

        department_id = request.GET.get('department_id')
        if department_id != None and department_id != '':
            kw['department_id'] = department_id

        major_id = request.GET.get('major_id')
        if major_id != None and major_id != '':
            kw['major_id'] = major_id

        class_id = request.GET.get('class_id')
        if class_id != None and class_id != '':
            kw['class_id'] = class_id

        student_grade = request.GET.get("student_grade")
        if student_grade != None and student_grade != '':
            kw['student_grade'] = student_grade

        student_data=Student.objects.filter(**kw).all()

        # print(student_data)


        if len(student_data) == 0:
            return JsonResponse(temp_result)

        temp_result["has_data"]=True

        student_dict={}
        for data in student_data:
            student_dict[data.student_id]=0
            student_score_data=Score.objects.filter(student_id=data.student_id).all()
            for score_data in student_score_data:
                if score_data.overall_score < 60:
                    student_dict[data.student_id] += int(
                        score_data.course_grade)
        
        result_data={}
        for key in student_dict:
            result_data[str(student_dict[key])]=[]
        
        for key in student_dict:
            result_data[str(student_dict[key])].append(key)
        temp_result['chart_data'] = result_data

        x_data=[]
        y_data={
            "数量":[]
        }
        # 处理x轴
        
        for key in result_data:
            # print(key)
            x_data.append(int(key))
        x_data.sort()
        for index in range(len(x_data)):
            x_data[index]=str(x_data[index])
        

        # print(x_data)
        # 处理y轴
        for key in x_data:
            y_data['数量'].append(len(result_data[key]))
        
        chart_option=get_line(x_data,y_data,'数量/人','学分')
        temp_result['chart_option']=chart_option
        
        return JsonResponse(temp_result)
    else:
        temp_result = {
            "has_data": False
        }
        return JsonResponse(temp_result)

def get_student_depend_score(request):
    if request.method=="POST":
        result={}

        print("qingqiushuju:",request.POST.get("student_id"))


        student_id_list =json.loads(request.POST.get("student_id"))

        print(student_id_list)

        student_id_list.sort()
        temp_result=[]
        for data in student_id_list:
            student_data=Student.objects.get(student_id=data)
            temp={
                "student_id":data,
                "student_name": student_data.student_name,
            }
            temp_result.append(temp)
        result['has_data']=True
        result['data_list'] = temp_result
        return JsonResponse(result)
    else:
        result={'has_data':False}
        return JsonResponse(result)

def get_student_number(request):
    data=Student.objects.filter().all()
    return HttpResponse(str(len(data)))
