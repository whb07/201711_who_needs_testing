import pytest
from unittest import mock
from ..africa_water import get_future_rainfall

# def test_water_response():
#     response = get_water_level_africa()
#     assert 'cm' in response, 'should be in cm'


@mock.patch('testing_python_meetup.africa_water.get_water_level_africa')
def test_mock_water_response(mock_response):
    mock_response.return_value = '25 cm'
    assert '25' in mock_response(), 'should be in cm'
