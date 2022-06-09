from django.urls import path
from .views import Commits


urlpatterns = [
    path('list/', Commits.as_view(), name="list_all_commits"),
]
