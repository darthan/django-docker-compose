# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"


class Ejercicio1View(TemplateView):
    template_name = "ejercicio1.html"
