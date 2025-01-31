from django.urls import path
from .views import is_authenticated, add_tab, check_session

urlpatterns = [
    path('is_authenticated/', is_authenticated, name='is_authenticated'),
    path('add_tab/', add_tab, name='add_tab'),
    path('check_session/', check_session, name='check_session'),
]
