from django.contrib import admin
from .models import TimeTable, Place, BookedRoom

admin.site.register(TimeTable)
admin.site.register(Place)
admin.site.register(BookedRoom)


