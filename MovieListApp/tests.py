from json import JSONDecodeError
from unittest.mock import MagicMock, Mock

import requests
from django.core.cache import cache
from django.http import JsonResponse
from django.test import TestCase, RequestFactory

# Create your tests here.
from MovieListApp.views import movie_list


class MovieListTestCases(TestCase):
    def setUp(self):
        self.req = RequestFactory().get('/movies')
        self.people_list_resp = [{"id": "p1", "name": "person_1", "films": ["film_1_url"]},
                                 {"id": "p2", "name": "person_2", "films": ["film_1_url"]},
                                 {"id": "p3", "name": "person_3", "films": ["film_1_url"]}]
        self.film_list_resp = [{"id": "film_1", "title": "title_1", "url": "film_1_url"},
                               {"id": "film_2", "title": "title_2", "url": "film_2_url"}]
        pass

    def test_get_movie_list(self):
        cache.clear()

        def data_set(resource):
            if resource == 'films':
                return JsonResponse(self.film_list_resp, safe=False)
            if resource == 'people':
                return JsonResponse(self.people_list_resp, safe=False)
            return None

        requests.get = MagicMock(side_effect=data_set)

        res = movie_list(self.req, 'films', 'people')

        self.assertEqual(res.content, b'title_1\n\tperson_1\n\tperson_2\n\tperson_3\ntitle_2\n\t\n')

    def test_empty_response(self):
        cache.clear()

        requests.get = MagicMock(return_value=JsonResponse([], safe=False))

        res = movie_list(self.req, 'films', 'people')

        self.assertEqual(res.content, b'')

    def test_json_decode_error(self):
        cache.clear()

        requests.get = Mock(side_effect=JSONDecodeError("Error in JSON format", "", 0))

        res = movie_list(self.req, 'films', 'people')

        self.assertEqual(res.content, b'Problem with the Movie API')