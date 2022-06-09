from urllib import response
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from Utils.GitHubAPIRequests import GitHubAPIRequests
from .serializers import CommitsSerializers


# Commits views
class Commits(APIView):
    """
        API to list the commits in the repo.
        
        GET: 
            summary: Endpoint to List Commits
            description: Get the commits in the repo.
            responses:
                200:
                    description: List the commits.
    """
    
    def get(self, request, *args, **kwargs):
        github_api_requests = GitHubAPIRequests()
        commits = github_api_requests.get_commits()
        if not commits['success']:
            response = {
                "success": commits['success'],
                "message": commits['data']
            }
            return Response(response, commits['status_code'])
        commits_serializer = CommitsSerializers(commits['data'], many=True)
        response = {
            "success": commits['success'],
            "message": "List of all commits",
            "data": commits_serializer.data
        }
        return Response(response, status=commits['status_code'])
    