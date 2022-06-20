import jwt
from django.conf import settings
from django.http import JsonResponse

from accounts.models import School


def assert_login(func):
    def wrapper(self, request, *args, **kwargs):
        access_token = request.META.get('HTTP_AUTHORIZATION', None)

        if access_token is None:
            return JsonResponse({'messaege': 'NEED_LOGIN'}, status=401)

        try:
            payload = jwt.decode(access_token, settings.SECRET_KEY, algorithms=settings.JWT_ALGORITHM)
            school = School.objects.get(name=payload['name'])
            request.user = school
            return func(self, request, *args, **kwargs)

        except jwt.ExpiredSignatureError:
            return JsonResponse({'message': 'EXPIRED_TOKEN'}, status=401)

        except jwt.exceptions.DecodeError:
            return JsonResponse({'message': 'INVALID_TOKEN'}, status=401)

        except School.DoesNotExist:
            return JsonResponse({'message': 'INVALID_School'}, status=401)

    return wrapper