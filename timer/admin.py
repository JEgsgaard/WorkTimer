from django.contrib import admin
from .models import WeeklyHourDefault, HourlyGoals


class HourlyGoalsAdmin(admin.ModelAdmin):
    list_display = ("week_number", "weekly_hours")


admin.site.register(WeeklyHourDefault)
admin.site.register(HourlyGoals, HourlyGoalsAdmin)
