===========
django-trix
===========

`Trix rich text editor <http://trix-editor.org>`_ widget for Django.


------------
Installation
------------

It's on `PyPI <https://pypi.python.org/pypi/django-trix>`_::

    pip install django-trix


-----------------
Using django-trix
-----------------

django-trix includes both a form widget and a model admin mixin that enables
the rich text editor.

To enable the editor in the Django admin, inherit from TrixAdmin and set
the trix_admin attribute to a list of the fields that use an editor::

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
