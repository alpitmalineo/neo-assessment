from django import forms
from django.core.exceptions import ValidationError

from dashboard.models import Leave


class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ['from_date', 'to_date', 'reason']

        widgets = {
            'from_date': forms.DateInput(attrs={
                'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                'type':'date'}),
            'to_date': forms.DateInput(attrs={
                'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                'type':'date'}),
            'reason': forms.Textarea(attrs={
                'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                'placeholder': 'Enter Reason'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        from_date = cleaned_data.get('from_date')
        to_date = cleaned_data.get('to_date')

        if from_date and to_date:
            if from_date > to_date:
                raise ValidationError('The From Date cannot be later than the To Date.')
        return cleaned_data


class EditLeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ['status', ]
