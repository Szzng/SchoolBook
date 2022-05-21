from rest_framework.response import Response
from rest_framework import viewsets, mixins, status

from .models import TimeTable, Place, BookedTablets, LeftTablets
from .serializers import BookedTabletsSerializer
from .actions import updateLeftTabletsCount, getLeftTabletsCount


class BookedTabletsByDateViewSet(mixins.CreateModelMixin,
                                 mixins.DestroyModelMixin,
                                 mixins.ListModelMixin,
                                 viewsets.GenericViewSet):
    serializer_class = BookedTabletsSerializer

    def get_queryset(self):
        return BookedTablets.objects.all().order_by('time')

    def create(self, request, *args, **kwargs):
        for i in request.data['time.period']:
            date, created = TimeTable.objects.get_or_create(
                date=request.data['time.date'],
                period=i,
                id=request.data['time.date'] + '-' + str(i)
            )
            place = Place.objects.get(name=request.data['place.name'])
            bookedTablets = BookedTablets.objects.create(
                time=date,
                place=place,
                borrower=request.data['borrower'],
                quantity=request.data['quantity']
            )
            updateLeftTabletsCount(
                time=date,
                place=place,
                count=request.data['quantity'],
                increase=False
            )

        return Response(self.serializer_class(bookedTablets).data)

    def retrieve(self, request, pk):
        date = TimeTable.objects.filter(id__contains=pk).order_by('id')
        places = Place.objects.all()
        data = {}

        for period in date:
            dictByPeriod = {}
            for place in places:
                dictByPeriod[place.name] = {
                    'left': min(getLeftTabletsCount(period, place), place.totalQuantity),
                    'classes': list(
                        period.bookedtablets_set.filter(place=place.name).values('id', 'borrower', 'quantity'))
                }
            data[period.period] = dictByPeriod

        return Response(data)


class LeftTabletsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    def get_queryset(self):
        return LeftTablets.objects.all().order_by('time')

    def retrieve(self, request, pk):
        date = TimeTable.objects.filter(id__contains=pk).order_by('id')
        places = Place.objects.all()
        data = {}

        for place in places:
            lefts = [place.totalQuantity] * 6
            for period in date:
                lefts[period.period - 1] = getLeftTabletsCount(period, place)
            data[place.name] = lefts

        return Response(data)


class DestroyBookingViewSet(mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):

    def get_queryset(self):
        pass

    def destroy(self, request, pk, *args, **kwargs):
        tablet = BookedTablets.objects.get(id=pk)
        updateLeftTabletsCount(
            time=tablet.time,
            place=tablet.place,
            count=tablet.quantity,
            increase=True
        )
        tablet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
