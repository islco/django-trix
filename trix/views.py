from django.http import JsonResponse
from django.views.generic import View

from trix.forms import AttachmentForm
from .utils import is_valid_image_extension


class AttachmentView(View):
    def post(self, request, *args, **kwargs):
        form = AttachmentForm(self.request.POST, self.request.FILES)

        uploaded_attachment = request.FILES['file']

        if is_valid_image_extension(uploaded_attachment):
            if form.is_valid():
                print(self.request.FILES['file'])
                photo = form.save()
                data = {'url': photo.file.url}
            else:
                data = {}
            return JsonResponse(data)
        else:
            print("not valid")
            data = {}
            return JsonResponse(data)
