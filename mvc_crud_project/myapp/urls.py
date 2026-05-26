from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('studentform_data/', views.studentform_data, name='studentform_data'),
    path('studentdata_delete/', views.studentdata_delete, name='studentdata_delete'),
    path('student_data/', views.student_data, name='student_data'),
    path('studentdata_edit/', views.studentdata_edit, name='studentdata_edit'),
]