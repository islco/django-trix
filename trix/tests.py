import uuid
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client


class DjangoAdminTest(TestCase):

    def setUp(self):

        pwd = uuid.uuid4().hex
        user = User.objects.create_superuser('admin', 'admin@test.com', pwd)

        client = Client()
        client.login(username=user.username, password=pwd)

        self.client = client

    def test_django_admin(self):

        resp = self.client.get('/admin/trixtest/post/add/')

        self.assertContains(resp, '/static/trix/trix.css')
        self.assertContains(resp, '/static/trix/trix.js')
        self.assertContains(resp, '/static/trix/trix-django.js')

        self.assertContains(resp, '<trix-editor')


class TemplateTest(TestCase):

    def test_template(self):

        resp = self.client.get('/')

        self.assertContains(resp, '/static/trix/trix.css')
        self.assertContains(resp, '/static/trix/trix.js')
        self.assertContains(resp, '/static/trix/trix-django.js')

        self.assertContains(resp, '<trix-editor')
