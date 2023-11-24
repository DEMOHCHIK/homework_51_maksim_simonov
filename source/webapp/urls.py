from django.urls import path
from webapp.views import home, info, command


urlpatterns = [
    path('', home, name='home'),
    path('info/', info, name='info'),
    path('command/', command, name='command'),
]