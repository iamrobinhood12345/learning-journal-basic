# from pyramid.response import Response
from pyramid.view import view_config
import os
import io

HERE = os.path.dirname(__file__)

ENTRIES = [
    {"title": "Entry 1", "id": 1, "creation_date": "Dec 20, 2016",
    "body": "I learned some stuff about some other stuff."},
    {"title": "Entry 2", "id": 2, "creation_date": "Dec 20, 2016",
    "body": "I learned some stuff about some other stuff."},
    {"title": "Entry 3", "id": 3, "creation_date": "Dec 20, 2016",
    "body": "I learned some stuff about some other stuff."}
]

@view_config(route_name='list', renderer='templates/list.jinja2')
def index_page(request):
    # imported_text = open(os.path.join(HERE, 'static', 'ben-files', 'index.html')).read()
    # return imported_text
    all_stuff = ['lskdjf', 'sldkfjslfdj', 'lskdjflsjdf']
    return {"bag_list": all_stuff}

@view_config(route_name='detail', renderer='string')
def post_page(request):
    # imported_text = open(os.path.join(HERE, 'static', 'ben-files', 'post.html')).read()
    # return Response(imported_text)
    the_id = int(request.matchdict["id"])
    entry = ENTRIES[the_id]
    return {"entry": entry}

@view_config(route_name='about', renderer='string')
def about_page(request):
    imported_text = open(os.path.join(HERE, 'static', 'ben-files', 'about.html')).read()
    return Response(imported_text)

@view_config(route_name='update', renderer='string')
def update_page(request):
    imported_text = open(os.path.join(HERE, 'static', 'ben-files', 'contact.html')).read()
    return Response(imported_text)

@view_config(route_name='create', renderer='string')
def new_post_page(request):
    imported_text = open(os.path.join(HERE, 'static', 'ben-files', 'new_post.html')).read()
    return Response(imported_text)
