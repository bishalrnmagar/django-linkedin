from django import forms

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Django is amazing'}),
            'description': forms.Textarea(attrs={"class": "form-control", "rows": 3, 'placeholder': 'On regardance to ...'})
        }