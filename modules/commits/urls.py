from django.urls import path
from .views import Commits
from .views import detail_commit_by_sha
from .views import commits_by_branch


urlpatterns = [
    path('list/', Commits.as_view(), name="list_all_commits"),
    path('detail/<str:sha>', detail_commit_by_sha, name="detail_commits"),
    path('branch/<str:branch_name>', commits_by_branch, name="commits_by_branch"),
]
