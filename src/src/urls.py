"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# Package Installer
# PLUGIN: ANACONDA

from django.conf.urls import url
from django.contrib import admin

from apps.home.views import (HomeView, Ejercicio1View,
                             Ejercicio2View, Ejercicio3View, Ejercicio4View,
                             Ejercicio5View)

urlpatterns = [
    url(r'^$', HomeView.as_view()),
    url(r'^ejercicio/1$', Ejercicio1View.as_view()),
    url(r'^ejercicio/2$', Ejercicio2View.as_view()),
    url(r'^ejercicio/3$', Ejercicio3View.as_view()),
    url(r'^ejercicio/4$', Ejercicio4View.as_view()),
    url(r'^ejercicio/5$', Ejercicio5View.as_view()),
    url(r'^admin/', admin.site.urls),
]
