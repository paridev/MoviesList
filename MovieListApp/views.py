import json
from json import JSONDecodeError

import requests
from django.http import HttpResponse
from django.views.decorators.cache import cache_page


# Create your views here.
@cache_page(60, key_prefix='movie_list')
def movie_list(request, films_data_url, people_data_url):

    try:
        movies = json.loads(requests.get(films_data_url).content.decode('utf-8'))
        people = json.loads(requests.get(people_data_url).content.decode('utf-8'))
    except JSONDecodeError:
        return HttpResponse("Problem with the Movie API")

    try:
        films_dict = {}
        for movie in movies:
            films_dict[movie["url"]] = {"title": movie["title"], "people": []}

        for actor in people:
            for film in actor["films"]:
                current_cast = films_dict[film].get("people")
                current_cast.append(actor["name"])
                films_dict[film].update({'people': current_cast})

        display_content = ""
        for entry in films_dict.values():
            display_content += "{}\n\t{}\n".format(entry["title"], "\n\t".join(entry["people"]))

        return HttpResponse(display_content, content_type="text/plain")
    except KeyError:
        return HttpResponse("Problem with the Movie API response format")

