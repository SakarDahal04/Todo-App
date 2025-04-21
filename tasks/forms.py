from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Add new task...',
            }
        )
    )
    
    status = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
            }
        )
    )

    class Meta:
        model = Task
        fields = ['title', 'status']