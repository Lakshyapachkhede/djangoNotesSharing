from django.urls import path
from . import views

urlpatterns = [
    path('subjects/', view=views.subjects_list, name='subject_list'),
    path('notes/<int:pk>', view=views.note_detail, name='note_detail_json')
    
]

