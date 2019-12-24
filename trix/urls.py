from django.conf.urls import url
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt

from .views import AttachmentView

urlpatterns = [
    url(r'^attachment/$', staff_member_required(csrf_exempt(AttachmentView.as_view()))),
]
