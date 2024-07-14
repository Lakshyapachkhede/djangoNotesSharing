from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.note_list, name="note_list"),
    path('notes/<int:pk>', views.note_detail, name='note_detail'),
    path('subjects/<int:pk>', views.subject_notes, name='subject_notes'),
    path('search/', views.search_notes, name='search_notes' ),
    path('about/', views.about, name='about'),
    path("contact/", views.contact_view, name="contact"),
     path('success/', TemplateView.as_view(template_name='notes/success.html'), name='success'), 
]

