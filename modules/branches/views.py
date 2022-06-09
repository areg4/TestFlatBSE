from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from Utils.GitHubAPIRequests import GitHubAPIRequests
from .serializers import BranchesSerializers


# Branches views
class Branches(APIView):
    """
        API to list the branches in the repo.
        
        GET: 
            summary: Endpoint to List Branches
            description: Get the branches in the repo.
            responses:
                200:
                    description: List the branches.
    """
    
    def get(self, request, *args, **kwargs):
        github_api_requests = GitHubAPIRequests()
        branches = github_api_requests.get_branches()
        if not branches['success']:
            response = {
                "success": branches['success'],
                "message": branches['data']
            }
            return Response(response, status=branches['status_code'])
        branches_serializer = BranchesSerializers(branches['data'], many=True)
        response = {
            "success": branches['success'],
            "message": "List of all the branches",
            "data": branches_serializer.data
        }
        return Response(response, status=branches['status_code'])
    