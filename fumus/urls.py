from django.conf.urls import patterns, url

from fumus.views import SmokeTestView


urlpatterns = patterns('',
    url(r'^$', SmokeTestView.as_view()),
)
