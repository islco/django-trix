===========
django-trix
===========

`Trix rich text editor <http://trix-editor.org>`_ widget for Django.

Uses Trix 0.9.


------------
Installation
------------

It's on `PyPI <https://pypi.python.org/pypi/django-trix>`_::

    pip install django-trix


-----------------
Using django-trix
-----------------

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

django-trix includes both a form widget and a model admin mixin that enables
the rich text editor.

To enable the editor in the Django admin, inherit from TrixAdmin and set
the *trix_fields* attribute to a list of the fields that use an editor::

    from myawesomeblogapp.models import Post
    from trix.admin import TrixAdmin

    @admin.register(Post)
    class PostAdmin(TrixAdmin, admin.ModelAdmin):
        trix_fields = ('content',)


----
TODO
----

* A bunch of stuff!
* Attachment uploads
