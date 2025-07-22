from django.urls import path
from .views import TeamList, AnnouncementList, ProjectList, ContactMessageCreate, EventList

urlpatterns = [
    path('team/', TeamList.as_view(), name='team-list'),
    path('announcements/', AnnouncementList.as_view(), name='announcement-list'),
    path('projects/', ProjectList.as_view(), name='project-list'),
    path('contact/', ContactMessageCreate.as_view(), name='contact-message-create'),
    path('events/', EventList.as_view(), name='event-list'),
]
