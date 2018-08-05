from django.test import TestCase
from django.urls import reverse, resolve
from django.http import Http404
from rest_framework.test import APIClient 
from rest_framework import status
from datetime import datetime

from .models import Meeting
from datetime import datetime

import pdb

class ModelTestCase(TestCase):

    def setUp(self):
        meeting_name = 'Interview Andressa Sivolella'
        self.meeting = Meeting(
            name=meeting_name,
            date=datetime.now()
        )

    def test_model_should_create_an_instance(self):
        actual = Meeting.objects.count()
        self.assertEqual(actual, 0),
        
        self.meeting.save()

        actual = Meeting.objects.count()
        self.assertEqual(actual, 1)

        actual = Meeting.objects.filter(name="Interview Andressa Sivolella")
        self.assertEqual(actual.count(), 1)


class ViewTestCase(TestCase):

    def setUp(self):
        self.date = '15/08/2018 15:00'
        spot_time = datetime.strptime(self.date, '%d/%m/%Y %H:%M')

        self.client = APIClient()

        self.data = {
            'name': 'tech definitions project a',
            'date': spot_time
        }

    def test_post_meeting(self):
        response = self.client.post(
            reverse('create'), self.data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        actual = Meeting.objects.filter(name='tech definitions project a')
        self.assertEqual(actual.count(), 1)

        actual_date = datetime.strftime(actual[0].date, '%d/%m/%Y %H:%M')
        self.assertEqual(actual_date, self.date) 

    def test_get_all_meetings(self):
        response = self.client.get(reverse('get_all'))

        # Assert status code is 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Post some data in order to check later `get` method
        data = {
            'name': 'metting from get meetings',
            'date': datetime.now()
        }

        self.client.post(
            reverse('create'), data, format='json'
        )
        
        # Get all meetings and assert returned content
        response = self.client.get(reverse('get_all'))

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], data['name'])

    def test_get_meeting_by_id_that_does_not_exist(self):
        # Assert status code 404
        response = self.client.get(
            reverse('get_by_id', args=[4]) # /meeting/4/
        )
        self.assertRaises(Http404)

    def test_get_meeting_by_id(self):
        date = '20/08/2018 10:00'

        data = {
            'name': 'meeting from get by id',
            'date': datetime.strptime(date, '%d/%m/%Y %H:%M')
        }
        self.client.post(
            reverse('create'), data, format='json'
        )

        all_meetings = self.client.get(reverse('get_all'))
        actual_id = all_meetings.data[0]['id']
        
        response = self.client.get(
            reverse('get_by_id', args=[actual_id]) # e.i. /meeting/1/
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['date'], "2018-08-20T10:00:00")
