from django.forms import ModelForm, ValidationError
from .models import Vacation
from django.contrib.admin.widgets import AdminDateWidget
from datetime import date


class VacationForm(ModelForm):
    class Meta:
        model = Vacation
        fields = ['city', 'travelers', 'cabin', 'start_travel', 'end_travel']
        widgets = {
            'start_travel': AdminDateWidget(),
            'end_travel': AdminDateWidget(),
        }

    # def clean(self):
    #     cleaned_data = super().clean()
    #     start_travel = cleaned_data['start_travel']
    #     end_travel = cleaned_data['end_travel']
    #
    #     # import pdb; pdb.set_trace()
    #     today = date.today()
    #     # import pdb; pdb.set_trace()
    #     if start_travel.date() < today:
    #         self.add_error('start_travel', ValidationError(
    #             "Can't choose a date in the past!"))
    #     elif end_travel.date() < start_travel.date():
    #         self.add_error('end_travel', ValidationError(
    #             "Pick a proper end date"))
