from django.urls import path, re_path
from . import views
"""Defines URL schemes for the_counter"""

app_name = 'the_counter'
urlpatterns = [
    # Home page
    path('', views.index, name="index"),

    # Budget parts
    path('budget/', views.budget, name="budget_parts"),

    # Income_Records
    path('budget/income/', views.income_records, name="income_records"),

    # Expenses_Records
    path('budget/expenses/', views.expenses_records, name="expenses_records"),

    # WishList_Records
    path('budget/wish_list/', views.wish_list, name="wish_list"),

    # New_Record
    path('budget/new_record/', views.new_record, name="new_record"),

    # Edit_Record
    re_path(r'^edit_record/(?P<record_id>\d+)/$', views.edit_record, name="edit"),

    # Delete_Record
    re_path(r'^delete_record/(?P<record_id>\d+)/$', views.delete_record, name="delete"),
]
