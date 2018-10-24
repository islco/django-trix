from django import forms
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import FormView

from trix.widgets import TrixEditor


class EditorForm(forms.Form):
    content = forms.CharField(widget=TrixEditor)


class EditorView(FormView):
    form_class = EditorForm
    template_name = 'index.html'


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^trix/', include('trix.urls')),
    url(r'^$', EditorView.as_view()),
]
