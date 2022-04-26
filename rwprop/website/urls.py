
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),

    path('structure', views.structure, name='structure'),
    path('sections', views.sections, name='sections'),
    path('bureau', views.bureau, name='bureau'),

    path('work', views.work, name='work'),
    path('announcement', views.announcement, name='announcement'),
    path('protocol', views.protocol, name='protocol'),
    path('plan', views.plan, name='plan'),
    path('achievements', views.achievements, name='achievements'),
    path('suggestions', views.suggestions, name='suggestions'),
    path('participation', views.participation, name='participation'),
    # path('docs', views.docs, name='docs'),
    # path('decisions', views.decisions, name='decisions'),
    path('reports', views.reports, name='reports'),
    path('other', views.other, name='other'),

    path('community', views.community, name='community'),
    path('conferences', views.conferences, name='conferences'),
    path('seminars', views.seminars, name='seminars'),
    path('projects', views.projects, name='projects'),

    path('contacts', views.contacts, name='contacts'),

    path('settings', views.settings, name='settings'),

    path('download/', views.download, name='download'),

    path('search/', views.search, name='search'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
