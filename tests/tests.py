# -*- coding: utf-8 -*-


from django.test import TestCase
from .models import MyForm
from django_remote_jsonschema_forms import RemoteJSONSchemaForm


class FormTest(TestCase):

    def test_form_returns_dict(self):
        form = MyForm()
        remote_form = RemoteJSONSchemaForm(form)

        self.assertTrue(isinstance(remote_form, dict))
