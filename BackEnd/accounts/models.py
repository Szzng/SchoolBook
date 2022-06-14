from random import random

from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db import models


def create_school_code():
    school_code = random.randint(1000, 9999)
    while School.objects.filter(code=school_code).exists():
        school_code = random.randint(1000, 9999)
    return school_code


class School(models.Model):
    code = models.PositiveBigIntegerField(primary_key=True, default=create_school_code)
    name = models.CharField(max_length=30, unique=True,)


class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, school, email, password):
        if not email:
            raise ValueError("이메일 주소를 입력해주세요.")
        if not school:
            raise ValueError("학교를 입력해주세요.")

        schoolObject = School.objects.create(name=school)
        user = self.model(school=schoolObject, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, school, email, password):
        user = self.create_user(school=school, email=email, password=password)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    objects = MyUserManager()

    school = models.OneToOneField(School, related_name='school', on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "school"
