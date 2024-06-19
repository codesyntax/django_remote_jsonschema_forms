# -*- coding: utf-8 -*-


from django.test import TestCase
from .models import MyForm
from ..forms import RemoteJSONSchemaForm


class FormTest(TestCase):

    def test_form_returns_dict(self):
        form = MyForm()
        remote_form = RemoteJSONSchemaForm(form)

        self.assertTrue(isinstance(remote_form, dict))
