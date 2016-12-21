import pytest
from pyramid import testing

@pytest.fixture
def req():
    the_request = testing.DummyRequest()
    return the_request

def test_home_page_renders_file_data(req):
    """My home page view returns some data."""
    from .views import index_page
    response = index_page(req)
    assert "<title>Learning Journal</title>" in response
