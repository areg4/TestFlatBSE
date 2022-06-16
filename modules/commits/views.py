import logging
from urllib import response
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
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
                200: List commits.
                400: Bad Request
                401: Unauthorized
                404: Not Found
                408: Request Timeout
                500: Internal Server Error
    """
    
    @swagger_auto_schema(
        operation_description="Get the commits in the repo.",
        responses={
            200: "Ok",
            400: "Bad Request",
            401: "Unauthorized",
            404: "Not Found",
            408: "Request Timeout",
            500: "Internal Server Error"
        }
    )
    def get(self, request, *args, **kwargs):
        """
            Get the list of the commits in the repo.

        Returns:
            200: 
                description: List commits
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
        except Exception as e:
            logging.error(str(e))
            response = {
                "success": False,
                "message": "Something goes wrong. Please, contact to support."
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
@swagger_auto_schema(
    operation_description="Get commit details by SHA",
    method='get',
    responses={
        200: "Ok",
        400: "Bad Request",
        401: "Unauthorized",
        404: "Not Found",
        408: "Request Timeout",
        500: "Internal Server Error"
    }
)
@api_view(['GET'])
def detail_commit_by_sha(request, sha):
    """
        Get commit details by sha.

    Returns:
        200: 
            description: Commit details
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
        commit = github_api_requests.get_commit_by_sha(sha)
        if not commit['success']:
            response = {
                "success": commit['success'],
                "message": commit['data']
            }
            return Response(response, status=commit['status_code'])
        response = {
            "success": commit['success'],
            "message": "Detail of the commit",
            "data": commit['data']
        }
        return Response(response, status=commit['status_code'])
    except Exception as e:
        logging.error(str(e))
        response = {
            "success": False,
            "message": "Something goes wrong. Please, contact to support."
        }
        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
@swagger_auto_schema(
    method='get',
    operation_description="Get commits by branch",
    responses={
        200: "Ok",
        400: "Bad Request",
        401: "Unauthorized",
        404: "Not Found",
        408: "Request Timeout",
        500: "Internal Server Error"
    }
)
@api_view(['GET'])
def commits_by_branch(request, branch_name):
    """
        Get commits by branch name.

    Returns:
        200: 
            description: Commits by branch name
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
        commits = github_api_requests.get_commit_by_branch(branch_name)
        if not commits['success']:
            response = {
                "success": commits['success'],
                "message": commits['data']
            }
            return Response(response, status=commits['status_code'])
        response = {
            "success": commits['success'],
            "message": "Commits by branch",
            "data": commits["data"]
        }
        return Response(response, status=commits['status_code'])
    except Exception as e:
        logging.error(str(e))
        response = {
            "success": False,
            "message": "Something goes wrong. Please, contact to support."
        }
        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
