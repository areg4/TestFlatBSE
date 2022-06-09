from django.urls import path
from .views import Pulls_Requests


urlpatterns = [
    path('list/', Pulls_Requests.as_view(), name="list_all_pull_requests"),
]
