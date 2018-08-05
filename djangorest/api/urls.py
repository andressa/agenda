from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MeetingsList, MeetingDetails

urlpatterns = {
    url(r'^meetings/$', MeetingsList.as_view(), name='create'),
    url(r'^meetings/$', MeetingsList.as_view(), name='get_all'),
    url(r'^meeting/(?P<id>\d+)/$', MeetingDetails.as_view(), name='get_by_id')
}

urlpatterns = format_suffix_patterns(urlpatterns)
