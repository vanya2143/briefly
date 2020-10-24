from django import forms
from .models import Link
from django.core.exceptions import ValidationError


class AddUserLinkForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddUserLinkForm, self).__init__(*args, **kwargs)

        self.fields['destination_link'].label = "Длинная ссылка"
        self.fields['source_link'].label = "Сокращенная ссылка"

    def clean_source_link(self):
        data = self.cleaned_data['source_link']
        # print(data)
        if Link.objects.filter(source_link=data):
            raise ValidationError('Сокращенная ссылка с таким адресом уже существует')
        return data

    def clean_destination_link(self):
        data = self.cleaned_data['destination_link']
        # print(len(data))
        if len(data) > 50:
            raise ValidationError('Убедитесь, что это значение содержит не более 250 символов (сейчас %s)' % len(data))
        return data

    class Meta:
        model = Link
        fields = ['destination_link', 'source_link']
