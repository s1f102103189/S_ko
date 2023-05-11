from django.urls import path
from . import views

app_name = 'attence'

urlpatterns = [
    path('check-in/<int:employee_id>/', views.check_in, name='check_in'),
    path('check-out/<int:employee_id>/', views.check_out, name='check_out'),
]
