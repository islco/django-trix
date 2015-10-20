from django.views.generic import View


class AttachmentView(View):
    def post(self, request, *args, **kwargs):
        print(request)
