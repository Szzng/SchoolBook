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
        for i in request.data['period']:
            timetable, created = TimeTable.objects.get_or_create(
                date=request.data['date'],
                period=i,
                id=request.data['date'] + '-' + str(i)
            )

            bookedTablets, created = BookedTablets.objects.get_or_create(
                time=timetable,
                place=request.data['place'],
                borrower=request.data['borrower'],
                quantity=request.data['quantity']
            )
        return Response(status=201)

    def retrieve(self, request, pk):
        timetable = TimeTable.objects.filter(id__contains=pk).order_by('id')
        places = ['전산실', '학습 준비물실']
        data = {}
        for period in timetable:
            dictByPeriod = []
            for place in places:
                dictByPeriod.append(list(period.bookedtablets_set.filter(place=place).values('borrower', 'quantity')))
                print(list(period.bookedtablets_set.filter(place=place).values('quantity')))
            data[period.period] = dictByPeriod

        return Response(data)
