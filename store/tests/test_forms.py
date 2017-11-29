import pytest
from django.test import RequestFactory
from mixer.backend.django import mixer
from datetime import date, timedelta
from ..forms import VacationForm


class TestVacationForm:
    def test_valid(self):
        data = {
            'city': 'PARIS',
            'travelers': 4,
            'cabin': 'ECONOMY',
            'start_travel': date(2018, 12, 25),
            'end_travel': date(2018, 12, 31)
        }
        # create form without any data
        form = VacationForm()
        # check if form is valid
        assert form.is_valid() is False, 'Should not be valid without data'
        # now pass in data
        form = VacationForm(data=data)
        # check if valid again
        assert form.is_valid(), 'Should be valid with proper data'

    # check for cities allowed to be submitted
    def test_city(self):
        data = {
            'city': 'BERLIN',
            'travelers': 4,
            'cabin': 'ECONOMY',
            'start_travel': date(2018, 12, 25),
            'end_travel': date(2018, 12, 31)
        }
        form = VacationForm(data=data)
        assert form.is_valid() is False, 'Should not allow BERLIN'

    # check for dates!
    def test_travel_dates(self):
        today = date.today()
        last_week = today - timedelta(7)
        data = {
            'city': 'PARIS',
            'travelers': 2,
            'cabin': 'ECONOMY',
            'start_travel': today,
            'end_travel': last_week,
        }
        form = VacationForm(data=data)
        assert form.is_valid() == False, 'cant travel in past YET!'
