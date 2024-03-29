from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("take_timestamp", views.new_timestamp, name="take_timestamp"),
    path("manual", views.manual_timestamp, name="manual_timestamp"),
    path("edit_day", views.edit_day, name="edit_day"),
    path("edit_all_days", views.edit_all_days, name="edit_all_days"),
    path("edit/<int:id>", views.edit_entry, name="edit_entry"),
    path("delete/<str:ids>", views.delete_entry_pair, name="delete"),
    path("week/<int:week_number>", views.show_week, name="show_week"),
    path("all_weeks", views.show_all_weeks, name="show_all_weeks"),
    path("overview", views.show_overview, name="show_overview"),
    
]
