from __future__ import unicode_literals
from django import forms
from django.contrib.admin import widgets as admin_widgets


class TrixEditor(forms.Textarea):

    def render(self, name, value, attrs=None):

        if attrs is None:
            attrs = {}
        attrs.update({'style': 'display: none;'})

        id_attr = attrs.get('id') or '{}_id'.format(name)
        html = super(TrixEditor, self).render(name, value, attrs)
        html += """<p><trix-editor input="{}" class="trix-content"></trix-editor></p>""".format(id_attr)
        return html

    class Media:
        css = {'all': ('trix/trix.css',)}
        js = ('trix/trix.js', 'trix/trix-django.js')
