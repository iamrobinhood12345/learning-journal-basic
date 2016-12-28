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
    some_html = "<p>Today I"
    assert some_html in str(response)


def test_post_view():
    from .views import post_page
    req.matchdict = {'id': '11'}
    info = post_page(req)
    assert "title" in str(info)


def test_update_view():
    from .views import update_page
    req.matchdict = {'id': '11'}
    info = update_page(req)
    assert "title" in str(info)


def test_new_post_view():
    from .views import new_post_page
    info = new_post_page(req)
    assert "title" in str(info)


def test_about_view():
    from .views import about_page
    info = about_page(req)
    assert "title" in str(info)


@pytest.fixture()
def testapp():
    """Create an instance of our app for testing."""
    from learning_journal_basic import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)


def test_layout_list(testapp):
    """Test that the contents of the list page contains something specific to this website."""
    response = testapp.get('/', status=200)
    html = response.html
    assert 'Ben Shields' in str(html)


def test_list_contents(testapp):
    """Test that the contents of the list page contains as many <h2> tags as journal entries."""
    from .views import ENTRIES
    response = testapp.get('/', status=200)
    html = response.html
    assert len(ENTRIES) == len(html.findAll('h2'))


def test_layout_post(testapp):
    """Test that the contents of the post page contains something specific to this website."""
    response = testapp.get('/journal/12', status=200)
    html = response.html
    assert 'Day 12' in str(html)


def test_layout_update(testapp):
    """Test that the contents of the update page contains something specific to this website."""
    response = testapp.get('/journal/11/edit-entry', status=200)
    html = response.html
    assert 'Day 11' in str(html)


def test_layout_new_post(testapp):
    """Test that the contents of the new post page contains something specific to this website."""
    response = testapp.get('/', status=200)
    html = response.html
    assert 'Ben Shields' in str(html)
