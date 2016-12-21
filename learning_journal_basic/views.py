# from pyramid.response import Response
from pyramid.view import view_config
import os
import io

HERE = os.path.dirname(__file__)

ENTRIES = [
    {"title": "Learning Journal - Day 11", "title1":"Pitches and Tools", "id": 11, "creation_date": "Dec 19, 2016",
     "body": "<p>Today I learned a good deal about my classmates. Each of us took turns pitching ideas for project week projects. I was very impressed with the creativity of my classmates. Several of their ideas seem like very good ones. I wish I could help out with all of them. Alas, decisions must be made, and we will eventually come to each work on one of a handful of projects. Such is life. We must choose decisively, and live with our choices for the rest of our days.</p><p>Avery and Patrick had awesome presentations. I learned about Itertools from Patrick, and can't wait for the chance to practice. Avery presented on an enhancement for Visual Studio that allows you to see documentation for functions as you are writing them. How cool is that!</p>"},
    {"title": "Entry 2", "title1": "New stuff learned","id": 2, "creation_date": "Dec 20, 2016",
     "body": "I learned some stuff about some other stuff."},
    {"title": "Entry 3", "title1": "New stuff learned", "id": 3, "creation_date": "Dec 20, 2016",
     "body": "I learned some stuff about some other stuff."}
]


@view_config(route_name='list', renderer='templates/list.jinja2')
def index_page(request):
    # imported_text = open(os.path.join(HERE, 'static', 'ben-files', 'index.html')).read()
    # return imported_text
    return {"ENTRIES": ENTRIES}


@view_config(route_name='detail', renderer='templates/post_tenplate.jinja2')
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
