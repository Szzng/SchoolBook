from django.utils.decorators import method_decorator
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

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
        Tool.objects.get_or_create(
            school=request.user,
            name=request.data['name'],
            quantity=request.data['quantity'],
            place=request.data['place']
        )
        return Response(status=status.HTTP_201_CREATED)


@method_decorator(assert_school_code, name='retrieve')
@method_decorator(assert_school_code, name='destroy')
class ToolRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer


@method_decorator(assert_school_code, name='list')
@method_decorator(assert_school_code, name='create')
class ToolBookingListCreate(ListCreateAPIView):
    serializer_class = ToolBookingSerializer

    def get_queryset(self):
        return ToolBooking.objects.all().order_by('period')

    def create(self, request, *args, **kwargs):
        tool = Tool.objects.get(name=request.data['tool'])

        for i in request.data['period']:
            period, created = Period.objects.get_or_create(
                date=request.data['date'],
                period=i,
                id=request.data['date'] + '-' + str(i)
            )

            booking = ToolBooking.objects.create(
                tool=tool,
                period=period,
                booker=request.data['booker'],
                quantity=request.data['quantity']
            )

            decreaseLeft(tool, period, request.data['quantity'])

        return Response(self.serializer_class(booking).data)


@method_decorator(assert_school_code, name='retrieve')
class ToolBookingRetrieve(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        tool = Tool.objects.filter(name=kwargs['toolId']).get()
        periods = Period.objects.filter(id__contains=kwargs['date']).order_by('id')

        data = {}
        for period in periods:
            data[period.period] = list(
                ToolBooking.objects.filter(
                    tool=tool.name,
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
        periods = Period.objects.filter(id__contains=kwargs['date']).order_by('id')
        tool = Tool.objects.filter(name=kwargs['toolId']).get()

        lefts = [tool.quantity] * 6
        for period in periods:
            lefts[period.period - 1] = getLeft(tool, period)

        return Response(lefts)
