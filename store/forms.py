from django.forms import ModelForm
from .models import Vacation
from django.contrib.admin.widgets import AdminDateWidget


class VacationForm(ModelForm):
    class Meta:
        model = Vacation
        fields = ['city', 'travelers', 'cabin', 'start_travel', 'end_travel']
        widgets = {
            'start_travel': AdminDateWidget(),
            'end_travel': AdminDateWidget(),
        }
