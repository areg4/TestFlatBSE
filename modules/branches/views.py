import logging
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
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
    
    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        try:
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
        except Exception as e:
            logging.error(str(e))
            response = {
                "success": False,
                "message": "Something goes wrong. Please, contact to support."
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
@api_view(['GET'])
@swagger_auto_schema()
def detail_branch(request, branch_name):
    try:
        github_api_requests = GitHubAPIRequests()
        branch = github_api_requests.get_branch_by_name(branch_name)
        if not branch['success']:
            response = {
                "success": branch['success'],
                "message": branch['data']
            }
            return Response(response, status=branch['status_code'])
        response = {
            "success": branch['success'],
            "message": "Detail of the branch",
            "data": branch['data']
        }
        return Response(response, status=branch['status_code'])
    except Exception as e:
        logging.error(str(e))
        response = {
            "success": False,
            "message": "Something goes wrong. Please, contact to support."
        }
        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)