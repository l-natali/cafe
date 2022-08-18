from django import forms
from django.core.exceptions import ValidationError

from .models import UserReservation
from django.core.validators import RegexValidator
import re


class UserReservationForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'name': 'name',
            'class': 'form-control',
            'id': 'name',
            'placeholder': 'Your Name ',
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

    def clean_email(self):
        data = self.cleaned_data

        if data['email'] == RegexValidator(regex=r'^(\d{3}[- ]?){2}\d{4}$'):
            return data['email']
        raise forms.ValidationError('Такой почты не существует')

    def clean_book_date(self):
        data = self.cleaned_data['book_date']

        if data == RegexValidator(regex=r'^/d{4}-/d{2}-/d{2}$'):
            return data
        raise forms.ValidationError('Неверный формат даты')

