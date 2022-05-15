from django.contrib import admin
from .models import TimeTable, BookedTablets

admin.site.register(TimeTable)
admin.site.register(BookedTablets)