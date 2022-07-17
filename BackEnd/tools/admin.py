from django.contrib import admin
from .models import Tool, ToolBooking, LeftQuantity

admin.site.register(Tool)
admin.site.register(ToolBooking)
admin.site.register(LeftQuantity)