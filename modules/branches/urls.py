from django.urls import path
from .views import Branches


urlpatterns = [
    path('list/', Branches.as_view(), name="list_all_branches"),
]
