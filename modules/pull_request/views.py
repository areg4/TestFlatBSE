import logging
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from Utils.GitHubAPIRequests import GitHubAPIRequests
from .serializers import PullRequestsSerializers


# Pull Requests views
class Pull_Requests(APIView):
    """
        API to list the Pull Requests in the repo.
        
        GET: 
            summary: Endpoint to List Pull Requests
            description: Get the PRs in the repo.
            responses:
                200:
                    description: List the Pull Requests.
    """
    
    def get(self, request, *args, **kwargs):
        try:
            github_api_requests = GitHubAPIRequests()
            pull_requests = github_api_requests.get_pull_requests()
            if not pull_requests['success']:
                response = {
                    "success": pull_requests['success'],
                    "message": pull_requests['data']
                }
                return Response(response, status=pull_requests['status_code'])
            pull_requests_serializer = PullRequestsSerializers(pull_requests["data"], many=True)
            response = {
                "success": pull_requests['success'],
                "message": "List of all Pull Requests",
                "data": pull_requests_serializer.data
            }
            return Response(response, status=pull_requests['status_code'])
        except Exception as e:
            logging.error(str(e))
            response = {
                "success": False,
                "message": "Something goes wrong. Please, contact to support."
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    