from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_notes, name='notes.all'),
    path('create', views.create_note, name='notes.create'),
    path('<int:pk>', views.get_notes_by_id, name='notes.detail'),
    path('<int:pk>/edit', views.update_notes_by_id, name='notes.edit'),
    path('<int:pk>/delete', views.delete_notes_by_id, name='notes.delete'),
    path('public/<int:pk>', views.get_public_notes_by_id, name='public.notes.detail')
]