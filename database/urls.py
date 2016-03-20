__author__ = 'anjaneyulu'

from django.conf.urls import patterns, url
from . import views
urlpatterns = [
    url(r'^$', views.home , name='home'),
    url(r'^company/(?P<slug>[\w-]+)/$', views.company, name='company'),
    url(r'^practice/(?P<slug>[\w-]+)/$', views.topic, name='topic'),
    url(r'^practice/(?P<topic>[A-Za-z0-9_-]+)/(?P<sub_topic>[A-Za-z0-9_-]+)/$', views.sub_topic, name='sub_topic_test'),
    url(r'^practice/technical/(?P<topic>[A-Za-z0-9_-]+)/(?P<sub_topic>[A-Za-z0-9_-]+)/$', views.technical, name='technical'),
    url(r'^interview/tips/$', views.interview, name='interview'),
    url(r'^company/(?P<slug>[\w-]+)/(?P<date_slug>[0-9]+-[0-9]+-[0-9]+)/test/start/$', views.company_test_start, name='company_test_start'),
    url(r'^company/(?P<slug>[\w-]+)/(?P<date_slug>[0-9]+-[0-9]+-[0-9]+)/test/view/$', views.company_test_view, name='company_test_view'),
    url(r'^privacy-policy/$', views.privacy_policy , name='privacy_policy'),
    url(r'^robots.txt$', views.robot , name='robot'),
    url(r'^sitemap.xml$', views.sitemap, name='sitemap'),
    url(r'^googlea95613a6b3c4ff8a.html$', views.google_verification, name='google_verification'),
]
