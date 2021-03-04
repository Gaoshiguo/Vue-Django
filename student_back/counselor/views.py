from django.shortcuts import render, HttpResponse
from student.models import ClassInfo, Major, Department
from django.http import JsonResponse

# Create your views here.


def index(request):
    return HttpResponse("This is counselor index")


# 返回所有的年级，班级，院系和专业
def get_all_school_information(request):
    if request.method == "GET":
        all_school_data = {
            "has_data": True,
            "data_list": {
                "department_list": [],
                "grade_list": [],
                "class_list": [],
                "major_list": [],
            }
        }
        for each_department in Department.objects.all():
            all_school_data["data_list"]["department_list"].append({
                "department_id":each_department.department_id,
                "department_name":each_department.department_name
            })
        
        for each_major in Major.objects.all():
            all_school_data["data_list"]["major_list"].append({
                "major_id":each_major.major_id,
                "major_name":each_major.major_name
            })
        
        for each_class in ClassInfo.objects.all():
            all_school_data["data_list"]["class_list"].append({
                "class_id":each_class.class_id,
                "class_name":each_class.class_name
            })
            grade = each_class.class_id[4:8]
            if grade not in all_school_data["data_list"]["grade_list"]:
                all_school_data["data_list"]["grade_list"].append(grade)

        all_school_data["data_list"]["grade_list"].sort()
        all_school_data["data_list"]["class_list"] = sorted(
            all_school_data["data_list"]["class_list"],key=lambda x:x['class_id'])
        all_school_data["data_list"]["department_list"]=sorted(
            all_school_data["data_list"]["department_list"],key=lambda x:x['department_id']
        )
        all_school_data["data_list"]["major_list"]=sorted(
            all_school_data["data_list"]["major_list"],key=lambda x:x['major_id']
        )
        return JsonResponse(all_school_data, safe=False)
    return HttpResponse("OK")

