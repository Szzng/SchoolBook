from django.contrib import admin
from .models import Tool, Period, ToolBooking, LeftTool

admin.site.register(Tool)
admin.site.register(Period)
admin.site.register(ToolBooking)
admin.site.register(LeftTool)