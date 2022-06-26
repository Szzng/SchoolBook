from django.db import models
import random
import string


def generate_school_code():
    code = ''
    for i in range(10):
        code += str(random.choice(string.ascii_lowercase + string.digits))

    while School.objects.filter(code=code).exists():
        code = ''
        for i in range(10):
            code += str(random.choice(string.ascii_lowercase + string.digits))

    return code


class School(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=10, primary_key=True, default=generate_school_code)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
