from django.utils.decorators import method_decorator
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView, \
    RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from accounts.decorators import assert_school_code
from tools.actions import increaseLeft, getLeft, decreaseLeft
from tools.models import Period, ToolBooking, Tool
from tools.serializers import ToolSerializer, ToolBookingSerializer


@method_decorator(assert_school_code, name='list')
@method_decorator(assert_school_code, name='create')
class ToolListCreate(ListCreateAPIView):
    serializer_class = ToolSerializer

    def get_queryset(self):
        return Tool.objects.filter(school=self.request.user.code).order_by('name')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        if Tool.objects.filter(school=request.user, name=data['name']).exists():
            return Response(
                data={'detail': '이미 등록된 이름입니다.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        Tool.objects.create(
            school=request.user,
            name=data['name'],
            quantity=data['quantity'],
            place=data['place']
        )

        return Response(status=status.HTTP_201_CREATED)


@method_decorator(assert_school_code, name='retrieve')
@method_decorator(assert_school_code, name='update')
@method_decorator(assert_school_code, name='destroy')
class ToolRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = ToolSerializer
    lookup_field = 'name'

    def get_object(self):
        queryset = Tool.objects.filter(school=self.request.user.code)
        lookup_url_kwarg = 'name'
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)
        return obj


@method_decorator(assert_school_code, name='create')
class ToolBookingCreate(CreateAPIView):
    def create(self, request, *args, **kwargs):
        serializer = ToolBookingSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        tool = get_object_or_404(Tool, **{'school': request.user, 'name': data['tool']})

        for i in data['period']:
            period, created = Period.objects.get_or_create(
                school=request.user,
                date=data['date'],
                period=i,
                id=data['date'] + '-' + str(i)
            )

            decreaseLeft(tool, period, data['quantity'])

            ToolBooking.objects.create(
                tool=tool,
                period=period,
                booker=data['booker'],
                quantity=data['quantity']
            )

        data = {
            'school': request.user.name,
            'tool': tool.name,
            'period': data['period'],
            'quantity': data['quantity']
        }

        return Response(data, status=status.HTTP_201_CREATED)


@method_decorator(assert_school_code, name='retrieve')
class ToolBookingRetrieve(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        tool = get_object_or_404(Tool, **{'school': request.user, 'name': kwargs['tool']})
        periods = Period.objects.filter(school=request.user, id__contains=kwargs['date']).order_by('id')

        data = {}
        for period in periods:
            data[period.period] = list(
                ToolBooking.objects.filter(
                    tool=tool.id,
                    period=period.id
                ).values('id', 'booker', 'quantity'))

        return Response(data)


@method_decorator(assert_school_code, name='destroy')
class ToolBookingDestroy(DestroyAPIView):
    def destroy(self, request, *args, **kwargs):
        booking = ToolBooking.objects.get(id=kwargs['bookingId'])
        increaseLeft(booking.tool, booking.period, booking.quantity)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@method_decorator(assert_school_code, name='retrieve')
class AvailableLeftRetrieve(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        tool = get_object_or_404(Tool, **{'school': request.user, 'name': kwargs['tool']})
        periods = Period.objects.filter(school=request.user, id__contains=kwargs['date']).order_by('id')

        lefts = [tool.quantity] * 6
        for period in periods:
            lefts[period.period - 1] = getLeft(tool, period)

        return Response(lefts)
