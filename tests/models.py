# -*- coding: utf-8 -*-
from django import forms
from django.db import models


class Task(models.Model):
    text = models.TextField("Text")
    email = models.TextField("Text")


class MyForm(forms.ModelForm):

    class Meta:
        model = Task
