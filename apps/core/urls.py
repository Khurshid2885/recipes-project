from django.urls import path

from apps.core.views import HelloView


urlpatterns  = [
    path('', view=HelloView.as_view(), name='hello')
]