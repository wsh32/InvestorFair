"""investorfair URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from . import connect
from . import views

urlpatterns = [
    # Portal
    url(r'^$', views.portal),

    # Website
    url(r'^site/$', views.website.home),
    url(r'^site/attractions/$', views.website.attractions),
    url(r'^site/visit/$', views.website.visit),
    url(r'^site/team/$', views.website.team),
    url(r'^site/faq/$', views.website.faq),
    url(r'^site/resources/$', views.website.resources),

    # Commercial
    url(r'^commercial/$', views.commercial),

    # Display
    url(r'^display/cover/$', views.display.cover),
    url(r'^display/overview/$', views.display.overview),
    url(r'^display/attractions/$', views.display.attractions),
    url(r'^display/finance/$', views.display.finance),

    url(r'^state/$', connect.get_state),
    url(r'^set/$', connect.set_state),
    url(r'^admin/$', views.admin),
]
