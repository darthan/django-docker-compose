# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"


class AristidesView(TemplateView):
    template_name = "home_2.html"


class Paso3View(TemplateView):
    template_name = "paso3.html"