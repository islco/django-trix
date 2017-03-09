from django.db import models

from trix.widgets import TrixEditor


class TrixField(models.TextField):

    def formfield(self, **kwargs):
        kwargs.update({'widget': TrixEditor})
        return super(TrixField, self).formfield(**kwargs)
