from pyramid.response import Response
import os

HERE = os.path.dirname(__file__)

def file_page(request):
    imported_text = open(os.path.join(HERE, 'sample.html')).read()
    return Response(imported_text)

def home_page(request):
    return Response("This is my first view!")

def includeme(config):
    config.add_view(home_page, route_name='home')
    config.add_view(file_page, route_name='file_page')