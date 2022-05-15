from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from .models import TimeTable, BookedTablets
from .serializers import TimeTableSerializer, BookedTabletsSerializer


class TabletsViewSet(mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):

    serializer_class = BookedTabletsSerializer

    def get_queryset(self):
        return BookedTablets.objects.all().order_by('time')

    def create(self, request, *args, **kwargs):
        print(request.data)
        timetable, created = TimeTable.objects.get_or_create(
            date=request.data['date'],
            period=request.data['period'], # list
            id=request.data['date'] + '-' + request.data['period']
        )

        bookedTablets, created = BookedTablets.objects.get_or_create(
            time=timetable,
            place=request.data['place'],
            borrower=request.data['borrower'],
            quantity=request.data['quantity']
        )
        return Response(self.serializer_class(bookedTablets).data)

    def retrieve(self, request, pk):
        timetable = TimeTable.objects.filter(id__contains=pk).order_by('id')
        data = []
        for period in timetable:
            dictByPeriod = {'period': period.period,
                            'place': [
                                {'name': '전산실', 'left': 0, 'classes': list(period.bookedtablets_set.filter(place='전산실').values())},
                                {'name': '준비물실', 'left': 0, 'classes': list(period.bookedtablets_set.filter(place='학습 준비물실').values())},
                            ]}
            data.append(dictByPeriod)

        return Response(data)

