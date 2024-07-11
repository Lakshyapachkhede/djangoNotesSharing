from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Note, Subject
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def paginate_notes(request, notes):
    paginator = Paginator(notes, 10)
    page = request.GET.get("page")

    try:
        paginated_notes = paginator.page(page)
    except PageNotAnInteger:
        paginated_notes = paginator.page(1)
    except EmptyPage:
        paginated_notes = paginator.page(paginator.num_pages)
    
    return paginated_notes




def note_list(request):
    notes = Note.objects.all().order_by('-uploaded_at')
    paginated_notes = paginate_notes(request, notes)
    return render(request, 'notes/note_list.html', {'title':"iNotes Download Notes",'heading':'All Notes','notes': paginated_notes})


def subject_notes(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    notes = subject.notes.all().order_by('-uploaded_at')
    return render(request, 'notes/note_list.html', {'title':f"Download {subject} Notes",'heading':f'{subject} Notes','subject': subject, 'notes': notes})



def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    response = HttpResponse(note.file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{note.file.name}"'
    return response


def search_notes(request):
    query = request.GET.get('q')
    if query:
        notes = Note.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)).order_by('-uploaded_at')
    else:
        notes = Note.objects.all().order_by('-uploaded_at')
    return render(request, 'notes/note_list.html', {'title':f"iNotes - Search Result for {query}",'heading':f'Search Result for {query}','notes': notes})
    

def about(request):
    return render(request, 'notes/about.html', {'title':'About iNotes'})