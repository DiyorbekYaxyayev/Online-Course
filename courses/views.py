from django.db.models import Count
from django.shortcuts import render
from django.views import View

from courses.models import Category, Course, Teacher, CourseComment


class HomeView(View):
    def get(self, request):
        top_categories = Category.objects.annotate(course_count=Count('courses')).order_by('-course_count')[:8]
        top_courses = Course.objects.annotate(pupils_count=Count('pupils')).order_by('-pupils_count')[:6]
        top_teachers = Teacher.objects.annotate(courses_count=Count('courses')).order_by('-courses_count')[:4]
        top_comments = CourseComment.objects.filter(rating=5).order_by('-created_at')[:3]

        context = {
            'top_categories': top_categories,
            'top_courses': top_courses,
            'top_teachers': top_teachers,
            'top_comments': top_comments,
        }

        return render(request, 'courses/index.html', context)

def courses(request):
    return render(request, 'courses/courses.html')

def course_detail(request):
    return render(request, 'courses/course-detail.html')

