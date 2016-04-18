"""serverBackend URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('SmartSecure.urls')),
    url(r'^login/(?P<linkpath>.*)$', 'SmartSecure.views.login', name='login'),
    url(r'^dashboard/$', 'SmartSecure.views.dashboard', name='dashboard'),
    url(r'^logout/$', 'SmartSecure.views.logout', name='logout'),
    url(r'^register/$', 'SmartSecure.views.register', name='register'),
    url(r'^help/$', 'SmartSecure.views.help', name='help'),
    url(r'^contact/$', 'SmartSecure.views.contact', name='contact'),
    url(r'^about/$', 'SmartSecure.views.about', name='about')
]
