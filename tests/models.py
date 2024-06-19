# -*- coding: utf-8 -*-
from django.db import models
from django import forms


class Task(models.Model):
    text = models.TextField("Text")
    email = models.TextField("Text")


class MyForm(forms.ModelForm):

    class Meta:
        model = Task
