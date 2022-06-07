from django.contrib import admin
from .models import Room, RoomBooking, FixedTimeTable, EmptyTimeTable, AvailableEvent

admin.site.register(Room)
admin.site.register(FixedTimeTable)
admin.site.register(EmptyTimeTable)
admin.site.register(AvailableEvent)
admin.site.register(RoomBooking)


