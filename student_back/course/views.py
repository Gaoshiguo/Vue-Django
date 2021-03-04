from django.shortcuts import render, HttpResponse
from student.models import Student, Score, Course
from django.http import JsonResponse

# Create your views here.


def index(request):
    return HttpResponse("This is the course index")


def get_current_student_is_failed(student_id):
    current_student_id = student_id
    if current_student_id is None or len(current_student_id) != 12:
        return HttpResponse("学号未给定或者学号错误")
    else:
        all_score_queryset = Score.objects.filter(
            student_id=current_student_id).all()
        for each_score in all_score_queryset:
            is_failed = "否" if each_score.overall_score >= 60 else "是"
            if is_failed == "是":
                return is_failed


def get_current_student_score(request):
    if request.method == "GET":
        current_student_id = request.GET.get("student_id")
        if current_student_id is None or len(current_student_id) != 12:
            return HttpResponse("学号未给定或者学号错误")
        else:
            all_score_queryset = Score.objects.filter(student_id=current_student_id).all()
            if len(all_score_queryset) == 0:
                score_list = {
                    "has_data": "fail",
                }
                return JsonResponse(score_list, safe=False)
            # print(all_score_queryset)
            score_list = {
                "has_data": "success",
                "data_list": [],
            }
            for each_score in all_score_queryset:
                # print(type(each_score))
                # print(each_score.course_id.course_id)
                is_failed = "否" if each_score.overall_score >= 60 else "是"
                temp_data = {
                    "course_id": each_score.course_id.course_id,
                    "course_name": Course.objects.filter(course_id=each_score.course_id.course_id)[0].course_name,
                    "course_grade": each_score.course_grade,
                    "overall_score": each_score.overall_score,
                    "get_grade": each_score.get_grade,
                    "is_failed": is_failed,  # 表示是否挂科
                }
                score_list['data_list'].append(temp_data)
            return JsonResponse(score_list, safe=False)
    else:
        score_list = {
            "has_data": "error",
        }
        return JsonResponse(score_list, safe=False)


def get_current_student_detail_score(request):
    if request.method == "GET":
        current_student_id = request.GET.get("student_id")
        course_id = request.GET.get("course_id")
        print("课程号:",course_id)
        if current_student_id is None or len(current_student_id) != 12:
            return JsonResponse({"has_data": False})
        if course_id is None:
            return JsonResponse({"has_data": False})
        else:
            all_score_queryset = Score.objects.filter(student_id=current_student_id,course_id=course_id).all()
            # print(all_score_queryset)
            course_name = Course.objects.get(course_id=course_id)
            course_name = course_name.course_name
            is_failed = "否" if all_score_queryset[0].overall_score >= 60 else "是"
            score_list = {
                "has_data": True,
                "data_list": {
                    "成绩编号": all_score_queryset[0].score_id,
                    "课程编号": course_id,
                    "课程名称": course_name,
                    "课程属性": all_score_queryset[0].course_type,
                    "课程学分": all_score_queryset[0].course_grade,
                    "上课学期": all_score_queryset[0].semester,
                    # 平时成绩
                    "平时成绩": all_score_queryset[0].part_time_score,
                    "期末成绩": all_score_queryset[0].exam_score,  # 期末成绩
                    # 综合成绩
                    "综合成绩": all_score_queryset[0].overall_score,
                    "所得学分": all_score_queryset[0].get_grade,
                    "是否挂科": is_failed,  # 表示是否挂科
                    "备注": all_score_queryset[0].postscript,  # 备注信息
                },
            }
            print(score_list)
            return JsonResponse(score_list)
            # return JsonResponse(score_list, safe=False)
    else:
        return JsonResponse({"has_data":False})

def get_course_number(request):
    data=Course.objects.filter().all()
    return HttpResponse(str(len(data)))