from django.conf.urls import include, url
from .views import AttachmentView


urlpatterns = [
    url(r'^attachment/$', AttachmentView.as_view()),
]
