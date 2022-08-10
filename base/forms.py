from django import forms
from .models import UserReservation


class UserReservationForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'name': 'name',
            'class': 'form-control',
            'id': 'name',
            'placeholder': 'Your Name',
            'data - rule': 'minlen:4',
            'data - msg': 'Please enter at least 4 chars',
        })
    )

    email = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'type': 'email',
            'class': 'form-control',
            'name': 'email',
            'id': 'email',
            'placeholder': 'Your Email',
            'data - rule': 'email',
            'data - msg': 'Please enter a valid email',

        })
    )

    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control',
            'name': 'phone',
            'id': 'phone',
            'placeholder': 'Your Phone',
            'data - rule': 'minlen:4',
            'data - msg': 'Please enter at least 4 chars',
        })
    )

    book_date = forms. DateField(widget=forms.DateInput(attrs={
        'type': 'text',
        'name': 'date',
        'class': 'form-control',
        'id': 'data',
        'placeholder': 'Date',
        'data - rule': 'minlen:4',
        'data - msg': 'Please enter at least 4 chars',
    }))

    book_time = forms.TimeField(widget=forms.TimeInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'name': 'time',
        'id': 'time',
        'placeholder': 'Time',
        'data - rule': 'minlen:4',
        'data - msg': 'Please enter at least 4 chars',
    }))

    persons = forms.IntegerField(widget=forms.NumberInput(attrs={
        'type': 'number',
        'class': 'form-control',
        'name': 'people',
        'id': 'people',
        'placeholder': '# of people',
        'data - rule': 'minlen:1',
        'data - msg': 'Please enter at least 1 chars'
    }))

    message = forms.CharField(
        max_length=500,
        widget=forms.Textarea(attrs={
            'type': 'message',
            'name': 'message',
            'class': 'form-control',
            'rows': '5',
            'placeholder': 'Message',
        })
    )

    class Meta:
        model = UserReservation
        fields = ('name', 'email', 'phone', 'book_date', 'book_time', 'persons', 'message')
