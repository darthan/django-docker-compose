# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"


class Ejercicio1View(TemplateView):
    template_name = "ejercicio1.html"


class Ejercicio2View(TemplateView):
    template_name = "ejercicio2.html"


class Ejercicio3View(TemplateView):
    template_name = "ejercicio3.html"
