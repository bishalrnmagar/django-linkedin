from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.db import models
from django.urls import reverse
from django.http import HttpResponse

from .models import Notes
from .forms import NotesForm

def get(model: models, pk=None):
    if pk is not None:
        return get_object_or_404(model, id=pk)
    return get_list_or_404(model)

def get_notes(request):
    notes = get(Notes)
    return render(request, 'notes/index.html', {'notes': notes})

def create_note(request):
    form = NotesForm
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes.all')
    return render(request, 'notes/form.html',{'form': form})   

def get_notes_by_id(request, pk):
    note = get(Notes, pk=pk)
    return render(request, 'notes/detail.html', {'note': note})

def update_notes_by_id(request, pk):
    instance = get(Notes, pk)   
    form = NotesForm(instance=instance)
    if request.method == 'POST':
        form = NotesForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse('notes.detail', kwargs={'pk': pk}))
    return render(request, 'notes/form.html', {'form': form})

def delete_notes_by_id(request, pk):
    instance = get(Notes, pk=pk)
    instance.delete()
    return redirect(reverse('notes.all'))
