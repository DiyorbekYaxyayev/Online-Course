from datetime import time, timedelta

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to="category/images/")
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="courses/images/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="courses", null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    teachers = models.ManyToManyField('Teacher', blank=True, related_name='courses')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_all_duration(self):
        lessons = self.lessons.all()
        total_seconds = sum(
            lesson.video_duration.hour * 3600 + lesson.video_duration.minute * 60 + lesson.video_duration.second
            for lesson in lessons
        )
        return timedelta(seconds=total_seconds)

    def get_average_rating(self):
        comments = self.comments.all()
        if comments:
            sum_rating = sum(
                comment.rating
                for comment in comments
            )
            return sum_rating / len(comments)
        return 5



class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to="lessons/videos/")
    video_duration = models.TimeField(default=time(0, 0, 0))  # Default 00:00:00
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.course.name} - {self.title}"


class CourseComment(models.Model):

    class RatingChoice(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="course_comments")
    rating = models.PositiveIntegerField(choices=RatingChoice.choices, default=RatingChoice.FIVE.value)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.name} ({self.rating})"


class Teacher(models.Model):
    fullname = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='teachers/photos/')
    direction = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='teachers')

    def __str__(self):
        return self.fullname
