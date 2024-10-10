from django.forms import ModelForm

from .models import Opera, Singer


class OperaForm(ModelForm):
    class Meta:
        model = Opera
        fields = ['title']


class SingerForm(ModelForm):
    class Meta:
        model = Singer
        fields = ['name', 'voice', 'opera']
