from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)


    def __str__(self):
        return self.name




class Note(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    file = models.FileField(upload_to='notes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey(Subject, related_name='notes', on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.title


