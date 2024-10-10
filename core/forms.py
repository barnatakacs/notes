from django import forms
from .models import NoteData

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = NoteData
        fields = ('name', 'description', 'tags',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'w-full pt-4 pb-0 px-6 rounded-xl border'
            }),
        }
