from rest_framework.response import Response
from rest_framework.decorators import api_view
from notes.models import Subject
from .serializers import SubjectSerializer

@api_view(['GET'])
def subjects_list(request):
    subjects = Subject.objects.all()
    serializer = SubjectSerializer(subjects, many=True)
    return Response(serializer.data)
