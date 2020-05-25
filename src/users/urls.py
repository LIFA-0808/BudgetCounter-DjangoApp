from django.urls import path

from . import views

"""Defines URL schemes for users"""

app_name = 'users'
urlpatterns = [
    # Registration
    path('register/', views.registration_view, name='register'),

    # Login page
    path('login/', views.login_view, name='login'),

    # Logout
    path('logout/', views.logout_view, name='logout'),

    # User Account
    path('user/', views.account_view, name='user'),

]
