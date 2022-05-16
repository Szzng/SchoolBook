from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from .models import TimeTable, BookedTablets, Place
from .serializers import TimeTableSerializer, BookedTabletsSerializer


class TabletsViewSet(mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = BookedTabletsSerializer

    def get_queryset(self):
        return BookedTablets.objects.all().order_by('time')

    def create(self, request, *args, **kwargs):
        for i in request.data['time.period']:
            timetable, created = TimeTable.objects.get_or_create(
                date=request.data['time.date'],
                period=i,
                id=request.data['time.date'] + '-' + str(i)
            )
            place = Place.objects.get(name=request.data['place.name'])
            bookedTablets, created = BookedTablets.objects.get_or_create(
                time=timetable,
                place=place,
                borrower=request.data['borrower'],
                quantity=request.data['quantity']
            )
        return Response(self.serializer_class(bookedTablets).data)

    def retrieve(self, request, pk):
        timetable = TimeTable.objects.filter(id__contains=pk).order_by('id')
        places = Place.objects.all()
        data = {}
        for period in timetable:
            dictByPeriod = {}
            for place in places:
                left = place.totalQuantity
                filteredByPlace = period.bookedtablets_set.filter(place=place.name)
                for i in filteredByPlace:
                    left -= i.quantity
                dictByPeriod[place.name] = {
                    'left': left,
                    'classes': list(filteredByPlace.values('borrower', 'quantity'))
                }
            data[period.period] = dictByPeriod

        return Response(data)
