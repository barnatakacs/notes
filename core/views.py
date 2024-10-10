from django.shortcuts import render, get_object_or_404, redirect
from .models import NoteData
from .forms import AddNoteForm
from django.db.models.functions import Coalesce
from django.db.models import Q

# Create your views here.


def index(request):
    query = request.GET.get('query', '')
    notes = NoteData.objects.annotate(
        sort_date=Coalesce('modified_at', 'created_at')
    ).order_by('-sort_date')

    if query:
        notes = NoteData.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)).annotate(
            sort_date=Coalesce('modified_at', 'created_at')
        ).order_by('-sort_date')

    return render(request, 'core/index.html', {
        'notes': notes,
        'query': query
    })


def detail(request, pk):
    note = get_object_or_404(NoteData, pk=pk)

    return render(request, 'core/detail.html', {
        'note': note
    })


def add(request):
    if request.method == 'POST':
        form = AddNoteForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('core:notes')
    else:
        form = AddNoteForm()

    return render(request, 'core/add.html', {
        'form': form,
        'title': 'Add'
    })


def delete(request, pk):
    note = get_object_or_404(NoteData, pk=pk)
    note.delete()

    return redirect('core:notes')


def edit(request, pk):
    note = get_object_or_404(NoteData, pk=pk)

    if request.method == 'POST':
        form = AddNoteForm(request.POST, request.FILES, instance=note)

        if form.is_valid():
            form.save()

            return redirect('core:detail', pk=note.id)
    else:
        form = AddNoteForm(instance=note)

    return render(request, 'core/add.html', {
        'form': form,
        'title': 'Edit'
    })
