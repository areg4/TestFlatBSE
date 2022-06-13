from django.urls import path
from .views import Pull_Requests
from .views import pull_request_by_number
from .views import merge_pull_request


urlpatterns = [
    path('', Pull_Requests.as_view(), name="pull_requests"),
    path('<int:pull_number>', pull_request_by_number, name="get_pull_request_by_number"),
    path('merge/<int:pull_number>', merge_pull_request, name="merge_pull_request_by_number"),
]
