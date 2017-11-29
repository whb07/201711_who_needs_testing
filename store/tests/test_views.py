import pytest
from django.test import RequestFactory
from mixer.backend.django import mixer
from datetime import date, timedelta
from selenium import webdriver
from time import sleep

def test_main_page(live_server):
    try:
        driver = webdriver.Chrome()
        driver.get(live_server.url)
        sleep(7)
        city_input = driver.find_element_by_id('id_city')
        city_input.send_keys('PARIS')
        travelers_input = driver.find_element_by_id('id_travelers')
        travelers_input.send_keys(4)
        cabin_input = driver.find_element_by_id('id_cabin')
        cabin_input.send_keys('FIRST')
        end_travel = driver.find_element_by_id('id_end_travel')
        end_travel.send_keys('2018-02-16')
        start_travel = driver.find_element_by_id('id_start_travel')
        start_travel.send_keys('2018-02-16')
        driver.find_element_by_id('submit').click()
        sleep(5)
        assert driver.find_element_by_css_selector('.title').text == 'Have Fun!'
    except:
        pass
    finally:
        driver.quit()
