from rest_framework import serializers
from notes.models import Subject
from notes.models import Note

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name')

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            'id',
            'title',
            'description',
            'file',
            'uploaded_at',
            'subject',
        )
