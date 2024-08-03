from rest_framework.response import Response
from rest_framework.decorators import api_view
from notes.models import Subject
from .serializers import SubjectSerializer
from .serializers import NoteSerializer
from django.shortcuts import get_object_or_404
from notes.models import Note

@api_view(['GET'])
def subjects_list(request):
    subjects = Subject.objects.all()
    serializer = SubjectSerializer(subjects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    serializer = NoteSerializer(note)
    return Response(serializer.data)