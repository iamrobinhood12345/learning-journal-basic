# from pyramid.response import Response
from pyramid.view import view_config
import os

HERE = os.path.dirname(__file__)

ENTRIES = [
    {"title": "Learning Journal - Day 12", "title1": "Slowly Getting Better", "id": '11', "creation_date": "Dec 20, 2016", "body": "<p>Today was a good day. I started off asking questions right away and was more attentive than I am most days. This felt really good. I'm going to try to ask as many questions as I can. I'm also going to volunteer for code review tomorrow. Today we also formed our groups for project week. Looks like Pysearch is happening after all! I have a good group going, with Marc, Casey, and Sera. This should be a lot of fun. My thoughts are that we should start small, and get a working implementation of a search engine going quickly, and design it in such a way that we can add features easily. Will said something about a simple search engine tutorial on Udacity. I will definitely ask him about this. The number one take away today would be that I should participate as much as I can, even if I don't feel like it, especially in the mornings. Another thing I realized is that a lot of computer science is actually getting good with getting a bunch of different things to work together -- different files, file systems, frameworks, functions that must speak to each other, having an account with the service you are using, and really taking all of these sort of things one step at a time. Overall, I can't wait to start working on Pysearch!</p>"},
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
