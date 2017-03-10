
def test_django_admin(admin_client):

    resp = admin_client.get('/admin/testapp/post/add/')

    assert b'/static/trix/trix.css' in resp.content
    assert b'/static/trix/trix.js' in resp.content
    assert b'/static/trix/trix-django.js' in resp.content
    assert b'<trix-editor' in resp.content


def test_template(client):

    resp = client.get('/')

    assert b'/static/trix/trix.css' in resp.content
    assert b'/static/trix/trix.js' in resp.content
    assert b'/static/trix/trix-django.js' in resp.content
    assert b'<trix-editor' in resp.content
