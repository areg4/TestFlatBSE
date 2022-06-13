import logging
from django.shortcuts import render
from drf_yasg import openapi
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
                200: List branches.
                400: Bad Request
                401: Unauthorized
                404: Not Found
                408: Request Timeout
                500: Internal Server Error
    """
    
    @swagger_auto_schema(
        operation_description="Get the branches in the repo.",
        responses={
            200: "Ok",
            400: "Bad request",
            401: "Unauthorized",
            404: "Not found",
            408: "Request Timeout",
            500: "Internal Server Error"
        }
    )
    def get(self, request, *args, **kwargs):
        """
            Get the list of the Branches in the repo.

        Returns:
            200: 
                description: List Branches
            400:
                description: Bad request
            401:
                description: Unauthorized
            404:
                description: Not found
            408: 
                description: Request Timeout
            500:
                description: Internal Server Error
        """
        
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
    
 
@swagger_auto_schema(
    operation_description="Get branch details",
    method='get',
    responses={
        200: "Ok",
        400: "Bad request",
        401: "Unauthorized",
        404: "Not found",
        408: "Request Timeout",
        500: "Internal Server Error"
    }
)
@api_view(['GET'])
def detail_branch(request, branch_name):
    """
        Get branch details by branch name.

    Returns:
        200: 
            description: Branch details
        400:
            description: Bad request
        401:
            description: Unauthorized
        404:
            description: Not found
        408: 
            description: Request Timeout
        500:
            description: Internal Server Error
    """
        
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
