from django.http import JsonResponse
from accounts.models import School


def assert_school_code(func):
    def wrapper(self, *args, **kwargs):
        code = self.META.get('HTTP_AUTHORIZATION', None)

        if code is None:
            return JsonResponse({'message': 'NEED_LOGIN'}, status=401)

        try:
            school = School.objects.get(code=code)
            self.user = school
            return func(self, *args, **kwargs)

        except School.DoesNotExist:
            return JsonResponse({'message': 'INVALID_SCHOOL'}, status=401)

    return wrapper
