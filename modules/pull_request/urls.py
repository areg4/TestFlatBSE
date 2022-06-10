from django.urls import path
from .views import Pull_Requests


urlpatterns = [
    path('list/', Pull_Requests.as_view(), name="list_all_pull_requests"),
]
