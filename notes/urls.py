from django.urls import path
from . import views

urlpatterns = [
    path("", views.note_list, name="note_list"),
    path('notes/<int:pk>', views.note_detail, name='note_detail'),
    path('subjects/<int:pk>', views.subject_notes, name='subject_notes'),
    path('search/', views.search_notes, name='search_notes' ),
    path('about/', views.about, name='about')
    
]

