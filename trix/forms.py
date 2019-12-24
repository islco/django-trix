from django import forms

from .models import Attachment


class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ('file',)
