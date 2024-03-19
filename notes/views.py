from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.db import models
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.decorators import login_required

from .models import Notes
from .forms import NotesForm

def get(model: models, pk=None, user=None):
    queryset = model.objects.filter(user=user, is_deleted=False)
    if pk is not None:
        queryset = model.objects.filter(id=pk, is_deleted=False, user=user)
        obj = get_object_or_404(queryset)
        return obj
    if queryset is None:
        return model()
    return queryset

@login_required(login_url='user.login')
def get_notes(request):
    notes = get(Notes, user=request.user)
    return render(request, 'notes/index.html', {'notes': notes})

@login_required(login_url='user.login')
def create_note(request):
    form = NotesForm
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            user = request.user
            obj = Notes(title=title, description=description, user=user)
            obj.save()
            return redirect('notes.all')
    return render(request, 'notes/form.html',{'form': form})   

@login_required(login_url='user.login')
def get_notes_by_id(request, pk):
    note = get(Notes, pk=pk, user=request.user)
    try: 
        return render(request, 'notes/detail.html', {'note': note})
    except Http404 as e:
        raise Http404("Requested resource not available")

@login_required(login_url='user.login')
def update_notes_by_id(request, pk):
    form = NotesForm
    instance = get(Notes, pk=pk, user=request.user)  
    if request.method == 'POST':
        form = NotesForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse('notes.detail', kwargs={'pk': pk}))
    return render(request, 'notes/form.html', {'form': form})

@login_required(login_url='user.login')
def delete_notes_by_id(request, pk):
    instance = get(Notes, pk=pk, user=request.user)
    instance.is_deleted = True
    instance.save()
    return redirect(reverse('notes.all'))
    