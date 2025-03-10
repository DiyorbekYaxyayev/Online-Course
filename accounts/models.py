from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.managers import UserManager
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(
        "Email Address",
        unique=True,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    photo = models.ImageField(upload_to='students/photos/', null=True, blank=True)
    courses = models.ManyToManyField('courses.Course', blank=True, related_name='pupils')

    objects = UserManager()

    def __str__(self):
        return self.email
