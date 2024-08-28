from django.urls import path
from newapp.views import *

urlpatterns = [
    path('', table, name='table'),
    path('create/', create_task, name='create'),   
    path('update/<pk>', update_task, name='update'),   
    path('delete/<pk>', delete_task, name='delete'),   
    path('completed/<pk>', task_complete, name='complete'),
    path('pending/<pk>', task_pending, name='pending'),

    path('employee/', employee_table, name='employee_table'),
    path('employee_create/', employee_create, name='employee_create'),
]

