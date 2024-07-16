from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Note, Subject
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


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
    note.total_downlods += 1
    note.save()
    return response


def search_notes(request):
    query = request.GET.get('q')
    if query:
        notes = Note.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)).order_by('-uploaded_at')
    else:
        notes = Note.objects.all().order_by('-uploaded_at')
    total_results = len(notes)
    notes = paginate_notes(request, notes)
    return render(request, 'notes/note_list.html', {'title':f"iNotes - Search Result for {query}",'heading':f'Search Result for {query}({total_results})','notes': notes,'query':query})
    

def about(request):
    return render(request, 'notes/about.html', {'title':'About iNotes'})


def contact_view(request):
    if request.method == 'POST':
        print(""*30 , 'inside post')
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(""*30 , 'inside valid')

            # email to site owner
            send_mail(
                subject=f'iNotes Contact from {name}',
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],
            )
            print(""*30 , 'inside owner')

            #email to sender
            send_mail(
                subject='Thank you for contacting iNotes',
                message=f'Dear {name},\n\nThank you for reaching out to us. We have received your request and will get back to you shortly.\n\nBest regards,\nLakshya Pachkhede\niNotes',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
            )
            print(""*30 , 'inside sender')

            return redirect('success')
        
    else:
        form = ContactForm()
        print(""*30 , 'inide else')

        
    return render(request, 'notes/contact.html', {'form': form, 'heading':'Contact Us', 'title':'Contact iNotes'})
