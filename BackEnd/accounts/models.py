import random
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models


def create_school_code():
    code = random.randint(100, 9999)
    while School.objects.filter(code=code).exists():
        code = random.randint(100, 9999)
    return code


class SchoolUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, name, password):
        if not name:
            raise ValueError("학교명을 입력해주세요.")

        school = self.model(name=name)
        school.code = create_school_code()
        school.password = make_password(password)
        school.save(using=self._db)
        return school

    def create_superuser(self, code, password):
        school = self.model(name='SuperUser', code=code)
        school.password = make_password(password)
        school.is_staff = True
        school.is_superuser = True
        school.save(using=self._db)
        return school


class School(AbstractBaseUser, PermissionsMixin):
    objects = SchoolUserManager()

    name = models.CharField(max_length=30)
    code = models.PositiveBigIntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "code"

    def __str__(self):
        return self.name + '/' + str(self.code)


class Ip(models.Model):
    ip = models.CharField(max_length=16, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
