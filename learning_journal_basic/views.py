from pyramid.response import Response
import os

HERE = os.path.dirname(__file__)

def index_page(request):
    imported_text = open(os.path.join(HERE, 'static', 'ben-files', 'index.html')).read()
    return Response(imported_text)

def post_page(request):
    imported_text = open(os.path.join(HERE, 'static', 'ben-files', 'post.html')).read()
    return Response(imported_text)

def about_page(request):
    imported_text = open(os.path.join(HERE, 'static', 'ben-files', 'about.html')).read()
    return Response(imported_text)

def contact_page(request):
    imported_text = open(os.path.join(HERE, 'static', 'ben-files', 'contact.html')).read()
    return Response(imported_text)

def new_post_page(request):
    imported_text = open(os.path.join(HERE, 'static', 'ben-files', 'new_post.html')).read()
    return Response(imported_text)

def includeme(config):
    config.add_view(index_page, route_name='list')
    config.add_view(post_page, route_name='detail')
    config.add_view(about_page, route_name='about')
    config.add_view(contact_page, route_name='update')
    config.add_view(new_post_page, route_name='create')
