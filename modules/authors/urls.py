from django.urls import path
from .views import Authors


urlpatterns = [
    path('list/', Authors.as_view(), name="list_all_authors"),
]
