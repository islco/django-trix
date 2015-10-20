===========
django-trix
===========

`Trix rich text editor <http://trix-editor.org>`_ widget for Django.

Uses Trix 0.9.


Using django-trix
-----------------

django-trix includes both a form widget and a model admin mixin that enables
the rich text editor.

Admin
~~~~~

To enable the editor in the Django admin, inherit from TrixAdmin and set
the *trix_fields* attribute to a list of the fields that use an editor::

    from myawesomeblogapp.models import Post
    from trix.admin import TrixAdmin

    @admin.register(Post)
    class PostAdmin(TrixAdmin, admin.ModelAdmin):
        trix_fields = ('content',)


Forms and Templates
~~~~~~~~~~~~~~~~~~~

The editor can be used in forms and templates by adding the *TrixEditor* widget
to a form field::

    from django import forms
    from trix.widgets import TrixEditor

    class EditorForm(forms.Form):
        content = forms.CharField(widget=TrixEditor)

In the template, just use the form as you normally would, but be sure to
include the associated media::

    <!doctype html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Trix Editor Test</title>
            {{ form.media.css }}
        </head>
        <body>
            <form>
                {{ form }}
            </form>
            {{ form.media.js }}
        </body>
    </html>

CSS in head, JS at end of body, because you are a responsible developer.


Installation
------------

It's on `PyPI <https://pypi.python.org/pypi/django-trix>`_::

    pip install django-trix

Add to *INSTALLED_APPS*::

    INSTALLED_APPS = (
        ...
        'trix',
        ...
    )

Add route to *urls.py*::

    urlpatterns = [
        ...
        url(r'^trixorwhateveryouwant/', include('trix.urls')),
        ...
    ]


TODO
----

* A bunch of stuff!
* Attachment uploads
