# -*- coding: utf-8 -*-


from django.test import TestCase

from django_remote_jsonschema_forms import RemoteJSONSchemaForm

from .models import MyForm


class FormTest(TestCase):

    def test_form_returns_dict(self):
        form = MyForm()
        remote_form = RemoteJSONSchemaForm(form)

        self.assertTrue(isinstance(remote_form, dict))
