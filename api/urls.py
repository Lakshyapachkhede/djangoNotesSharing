from django.urls import path
from . import views

urlpatterns = [
    path('subjects/', view=views.subjects_list, name='subject_list')
    
]

