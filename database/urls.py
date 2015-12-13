__author__ = 'anjaneyulu'

from django.conf.urls import patterns, url
from django.conf.urls.static import static
from practiceplacementpapers import settings
from . import views
urlpatterns = [
    url(r'^$', views.home , name='home'),
    url(r'^company/(?P<slug>[\w-]+)/$', views.company, name='company'),
    url(r'^practice/(?P<slug>[\w-]+)/$', views.topic, name='topic'),
    url(r'^practice/(?P<topic>[A-Za-z0-9_-]+)/(?P<sub_topic>[A-Za-z0-9_-]+)/$', views.sub_topic, name='sub_topic_test'),
    url(r'^interview/tips/$', views.interview, name='interview'),
    url(r'^company/(?P<slug>[\w-]+)/(?P<date_slug>[0-9]+-[0-9]+-[0-9]+)/test/start/$', views.company_test_start, name='company_test_start'),
    url(r'^company/(?P<slug>[\w-]+)/(?P<date_slug>[0-9]+-[0-9]+-[0-9]+)/test/view/$', views.company_test_view, name='company_test_view'),
    url(r'^privacy_policy/$', views.privacy_policy , name='privacy_policy'),
]#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)