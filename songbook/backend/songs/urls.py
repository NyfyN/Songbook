from django.urls import path
from .views import is_authenticated, add_tab, check_session, get_tabs

urlpatterns = [
    path('is_authenticated/', is_authenticated, name='is_authenticated'),
    path('add_tab/', add_tab, name='add_tab'),
    path('get_tabs/', get_tabs, name='get_tabs'),
    path('check_session/', check_session, name='check_session'),
]
