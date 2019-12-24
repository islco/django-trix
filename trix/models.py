from django.db import models


class Attachment(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
