# from pyramid.response import Response
from pyramid.view import view_config
import os

HERE = os.path.dirname(__file__)

ENTRIES = [
    {"title": "Learning Journal - Day 11", "title1": "Pitches and Tools", "id": '11', "creation_date": "Dec 19, 2016", "body": "<p>Today I learned a good deal about my classmates. Each of us took turns pitching ideas for project week projects. I was very impressed with the creativity of my classmates. Several of their ideas seem like very good ones. I wish I could help out with all of them. Alas, decisions must be made, and we will eventually come to each work on one of a handful of projects. Such is life. We must choose decisively, and live with our choices for the rest of our days.</p><p>Avery and Patrick had awesome presentations. I learned about Itertools from Patrick, and can't wait for the chance to practice. Avery presented on an enhancement for Visual Studio that allows you to see documentation for functions as you are writing them. How cool is that!</p>"},
    {"title": "DNA Transcription", "title1": "ATGCATGCATGCATGCATGCATGC", "id": '10', "creation_date": "Dec 20, 2016", "body": "I learned some stuff about some other stuff."},
    {"title": "Itertools", "title1": "New stuff learned", "id": '9', "creation_date": "Dec 20, 2016", "body": "I learned some stuff about some other stuff."},
    {"title": "Lambda", "title1": "x = lambda x, y: x+ y", "id": '8', "creation_date": "Dec 20, 2016", "body": "I learned some stuff about some other stuff."},
    {"title": "Learning from our Mistakes: Journey of a Computer Scientist", "title1": "How to iterate on improvement in the learning of programming.", "id": '7', "creation_date": "Dec 20, 2016", "body": "I learned some stuff about some other stuff."},
]


@view_config(route_name='list', renderer='templates/list.jinja2')
def index_page(request):
    # imported_text = open(os.path.join(HERE, 'static', 'ben-files', 'index.html')).read()
    # return imported_text
    return {"ENTRIES": ENTRIES}


@view_config(route_name='detail', renderer='templates/post_template.jinja2')
def post_page(request):
    # imported_text = open(os.path.join(HERE, 'static', 'ben-files', 'post.html')).read()
    # return Response(imported_text)
    the_id = request.matchdict["id"]
    entry = filter(lambda x: x["id"] == the_id, ENTRIES)[0]
    return {"entry": entry}


@view_config(route_name='about', renderer='string')
def about_page(request):
    imported_text = open(os.path.join(HERE, 'static', 'ben-files', 'about.html')).read()
    return Response(imported_text)


@view_config(route_name='update', renderer='templates/update_template.jinja2')
def update_page(request):
    the_id = request.matchdict["id"]
    entry = filter(lambda x: x["id"] == the_id, ENTRIES)[0]
    return {"entry": entry}


@view_config(route_name='create', renderer='templates/new_post_template.jinja2')
def new_post_page(request):
    return {"ENTRIES": ENTRIES}
