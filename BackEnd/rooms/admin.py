from django.contrib import admin
from .models import Place, RoomBooking, FixedTimeTable, EmptyTimeTable, AvailableBooking

admin.site.register(Place)
admin.site.register(FixedTimeTable)
admin.site.register(EmptyTimeTable)
admin.site.register(AvailableBooking)
admin.site.register(RoomBooking)


