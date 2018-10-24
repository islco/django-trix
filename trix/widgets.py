from __future__ import unicode_literals

import django
from django import forms
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class TrixEditor(forms.Textarea):

    def render(self, name, value, attrs=None, renderer=None):

        if attrs is None:
            attrs = {}
        attrs.update({'style': 'visibility: hidden; position: absolute;'})

        if renderer is None and django.get_version() > "2.0":
            renderer = forms.get_default_renderer()

        params = {
            'input': attrs.get('id') or '{}_id'.format(name),
            'class': 'trix-content',
        }
        param_str = ' '.join('{}="{}"'.format(k, v) for k, v in params.items())

        if django.get_version() >= "2.0":
            html = super(TrixEditor, self).render(name, value, attrs, renderer=renderer)
        else:
            html = super(TrixEditor, self).render(name, value, attrs)
        html = format_html(
            '{}<p><trix-editor {}></trix-editor></p>',
            html,
            mark_safe(param_str))
        return html

    class Media:
        css = {'all': ('trix/trix.css',)}
        js = ('trix/trix.js', 'trix/trix-django.js')
