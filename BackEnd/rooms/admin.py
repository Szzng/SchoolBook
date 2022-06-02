from django.contrib import admin
from .models import Place, RoomBooking, FixedTimeTable, EmptyTimeTable, AvailableBookingEvent

admin.site.register(Place)
admin.site.register(FixedTimeTable)
admin.site.register(EmptyTimeTable)
admin.site.register(AvailableBookingEvent)
admin.site.register(RoomBooking)


