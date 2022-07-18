from django.utils.decorators import method_decorator
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView, \
    RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from accounts.decorators import assert_school_code
from tools.actions import increaseLeft, getLeft, decreaseLeft
from tools.models import ToolBooking, Tool
from tools.serializers import ToolSerializer, ToolBookingSerializer


@method_decorator(assert_school_code, name='list')
@method_decorator(assert_school_code, name='create')
class ToolListCreate(ListCreateAPIView):
    serializer_class = ToolSerializer

    def get_queryset(self):
        return Tool.objects.filter(school=self.request.user.code).order_by('name')

    def create(self, request, *args, **kwargs):
        requestData = self.request.data.copy()
        requestData['school'] = request.user.code
        serializer = self.get_serializer(data=requestData)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

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
        tool = get_object_or_404(Tool, **{'school': request.user, 'name': self.request.data['tool']})
        serializer = ToolBookingSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        for i in data['period']:
            ToolBooking.objects.create(
                tool=tool,
                date=data['date'],
                period=int(i),
                booker=data['booker'],
                quantity=data['quantity'],
                password=data['password']
            )
            decreaseLeft(tool, data['date'] + '-' + str(i), data['quantity'])

        responseData = {
            'tool': tool.name,
            'date': data['date'],
            'period': data['period'],
            'booker': data['booker'],
            'quantity': data['quantity'],
            'password': data['password']
        }

        return Response(responseData, status=status.HTTP_201_CREATED)


@method_decorator(assert_school_code, name='retrieve')
class ToolBookingsByDate(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        tool = get_object_or_404(Tool, **{'school': request.user, 'name': kwargs['tool']})
        bookings = ToolBooking.objects.filter(tool=tool.id, date=kwargs['date'])

        data = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
        for booking in bookings:
            data[booking.period].append({
                'id': booking.id,
                'booker': booking.booker,
                'quantity': booking.quantity
            })

        return Response(data)


@method_decorator(assert_school_code, name='destroy')
class ToolBookingDestroy(DestroyAPIView):
    def destroy(self, request, *args, **kwargs):
        booking = get_object_or_404(ToolBooking, id=kwargs['bookingId'])

        if booking.password != request.data['password']:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'detail': '잘못된 비밀번호입니다.'})

        increaseLeft(booking.tool, str(booking.date) + '-' + str(booking.period), booking.quantity)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@method_decorator(assert_school_code, name='retrieve')
class LeftQuantityRetrieve(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        tool = get_object_or_404(Tool, **{'school': request.user, 'name': kwargs['tool']})
        lefts = [0] * 6
        for i in range(6):
            lefts[i] = getLeft(tool, kwargs['date'] + '-' + str(i + 1))

        return Response(lefts)
