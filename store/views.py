from django.views.generic.edit import FormView
# from django.http import HttpResponseRedirect
from . import forms
# Create your views here.
from django.shortcuts import render


class CreateVacation(FormView):
	template_name = 'store/vacation_form.html'
	fields = ['city', 'travelers', 'cabin', 'start_travel', 'end_travel']
	form_class = forms.VacationForm
	success_url = '/thanks'


def thanks(request):
	return render(request, 'store/thanks.html')
