from .views import community_cfp_view
from .views import community_read_only_view
from .views import community_landing_view
from .views import CommunityCreate, CommunityUpdate
from .views import ParticipationUpdate
from .views import ProjectUpdate
from .views import project_read_only_view

from django.conf.urls import url

urlpatterns = [
    url(r'^communities/cfp/add/$', CommunityCreate.as_view(), name='community-add'),
    url(r'^communities/cfp/(?P<slug>[^/]+)/participate/$', ParticipationUpdate.as_view(), name='community-participate'),
    url(r'^communities/cfp/(?P<slug>[^/]+)/edit/$', CommunityUpdate.as_view(), name='community-update'),
    url(r'^communities/cfp/(?P<community_slug>[^/]+)/add/$', ProjectUpdate.as_view(), name='project-participate'),
    url(r'^communities/cfp/(?P<community_slug>[^/]+)/(?P<project_slug>[^/]+)/edit/$', ProjectUpdate.as_view(), name='project-participate'),
    url(r'^communities/cfp/(?P<community_slug>[^/]+)/(?P<project_slug>[^/]+)/$', project_read_only_view, name='project-read-only'),
    url(r'^communities/cfp/(?P<slug>[^/]+)/$', community_read_only_view, name='community-read-only'),
    url(r'^(?P<round_slug>[^/]+)/communities/(?P<slug>[^/]+)/$', community_landing_view, name='community-landing'),
    url(r'^communities/cfp/$', community_cfp_view, name='community-cfp'),
]