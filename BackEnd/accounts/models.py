from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models


class SchoolUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, name, password):
        if not name:
            raise ValueError("학교명을 입력해주세요.")

        school = self.model(name=name)
        school.password = make_password(password)
        school.save(using=self._db)
        return school

    def create_superuser(self, name, password):
        superuser = self.create_user(name, password)
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.save(using=self._db)
        return superuser


class School(AbstractBaseUser, PermissionsMixin):
    objects = SchoolUserManager()

    name = models.CharField(max_length=30, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "name"

    def __str__(self):
        return self.name


class Ip(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    ip = models.CharField(max_length=16, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
