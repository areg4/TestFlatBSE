from django.urls import path
from .views import Branches
from .views import detail_branch


urlpatterns = [
    path('list/', Branches.as_view(), name="list_all_branches"),
    path('detail/<str:branch_name>', detail_branch, name="detail_branch"),
]
