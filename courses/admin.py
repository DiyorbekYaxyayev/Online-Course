from django.contrib import admin

from .models import Category, Course, Lesson, CourseComment, Teacher
# Register your models here.


admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(CourseComment)
admin.site.register(Teacher)