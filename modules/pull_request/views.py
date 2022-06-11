import logging
from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .models import PullRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from Utils.GitHubAPIRequests import GitHubAPIRequests
from .serializers import PullRequestsSerializers
from .serializers import PostPullRequestSerializers
from .serializers import SavePullRequestSerializers


# Pull Requests views
class Pull_Requests(APIView):
    """
        API to list the Pull Requests in the repo.
        
        GET: 
            summary: Endpoint to List Pull Requests
            description: Get the PRs in the repo.
            responses:
                200: List Pull Requests.
                400: Bad Request
                401: Unauthorized
                404: Not Found
                408: Request Timeout
                500: Internal Server Error
        POST: 
            summary: Endpoint to Create a Pull Request
            description: Create a PR in the repo.
            responses:
                201: Pull Request created.
                400: Bad Request
                401: Unauthorized
                422: Conflict whit the pull request
                408: Request Timeout
                500: Internal Server Error
    """
    
    @swagger_auto_schema(
        operation_description="Get the PRs in the repo.",
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
            Get the list of the PRs in the repo.

        Returns:
            200: 
                description: List Pull requests
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
    
    
    @swagger_auto_schema(
        operation_description="Create a PR in the repo.",
        request_body=PostPullRequestSerializers,
        responses={
            201: "Pull Request created.",
            400: "Bad Request",
            401: "Unauthorized",
            408: "Request Timeout",
            422: "Conflict whit the pull request",
            500: "Internal Server Error"
        }
    )
    def post(self, request, *args, **kwargs):
        """
            Create a PR in the repo.

        Returns:
            201: 
                description: Pull request created
            400:
                description: Bad request
            401:
                description: Unauthorized
            408: 
                description: Request Timeout
            422: 
                description: Conflict whit the pull request
            500:
                description: Internal Server Error
        """
        
        try:
            post_pull_request_serializer = PostPullRequestSerializers(data=request.data)
            if not post_pull_request_serializer.is_valid():
                response = {
                    "success": False,
                    "message": post_pull_request_serializer.errors
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            github_api_requests = GitHubAPIRequests()
            data = {
                "title": post_pull_request_serializer.validated_data['title'],
                "body": post_pull_request_serializer.validated_data['description'],
                "head": "test/head",
                "base": "test/base"
            }
            post_pull_request = github_api_requests.post_pull_request(data)
            if not post_pull_request['success']:
                if post_pull_request['status_code'] == 422:
                    post_pull_request['data'] = "Conflict whit the pull request. Please contact to support."
                response = {
                    "success": post_pull_request['success'],
                    "message": post_pull_request['data']
                }
                return Response(response, status=post_pull_request['status_code'])
            save_pull_request_serializer = SavePullRequestSerializers(post_pull_request['data'])
            PullRequest.objects.create(**save_pull_request_serializer.data)
            response = {
                "success": post_pull_request['success'],
                "message": "Pull Request was created!",
                "data": save_pull_request_serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        except Exception as e:
            logging.error(str(e))
            response = {
                "success": False,
                "message": "Something goes wrong. Please, contact to support."
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
@swagger_auto_schema(
    method='get',
    operation_description="Get Pull Request By Number",
    manual_parameters=[
        openapi.Parameter('pull_number', openapi.IN_PATH, 
                          description="Pull Number", 
                          type=openapi.TYPE_INTEGER)
    ],
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
def pull_request_by_number(request, pull_number):
    """
        Get the Pull request by number.

    Returns:
        200: 
            description: Pull request
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
        pull_request = github_api_requests.get_pull_request_by_number(pull_number)
        if not pull_request['success']:
            response = {
                "success": pull_request['success'],
                "message": pull_request['data']
            }
            return Response(response, status=pull_request['status_code'])
        pull_request_serializer = PullRequestsSerializers(pull_request['data'])
        response = {
            "success": pull_request['success'],
            "message": "Pull Request",
            "data": pull_request_serializer.data
        }
        return Response(response, status=pull_request['status_code'])
    except Exception as e:
        logging.error(str(e))
        response = {
            "success": False,
            "message": "Something goes wrong. Please, contact to support."
        }
        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
@swagger_auto_schema(
    method='put',
    operation_description="Merge a pull request",
    manual_parameters=[
        openapi.Parameter('pull_number', openapi.IN_PATH, 
                          description="Pull Number", 
                          type=openapi.TYPE_INTEGER)
    ],
    responses={
        200: "Ok",
        400: "Bad Request",
        401: "Unauthorized",
        408: "Request Timeout",
        422: "Conflict whit the pull request",
        500: "Internal Server Error"
    }
)
@api_view(['PUT'])
def merge_pull_request(request, pull_number):
    """
        Merge the Pull request in the repo.

    Returns:
        200: 
            description: Merge the pull request
        400:
            description: Bad request
        401:
            description: Unauthorized
        408: 
            description: Request Timeout
        422: 
            description: Conflict whit the pull request
        500:
            description: Internal Server Error
    """
    
    try:
        if not PullRequest.objects.filter(number=pull_number):
            response = {
                "success": False,
                "message": f"Pull request {pull_number}, does not exist in the internal record. Please try with other pull number or contact support"
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        
        if PullRequest.objects.filter(number=pull_number)[0].status == "merged":
            response = {
                "success": False,
                "message": f"Pull request {pull_number} is merged."
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
        github_api_requests = GitHubAPIRequests()
        pull_request = github_api_requests.merge_pull_request(pull_number)
        if not pull_request['success']:
            if pull_request['status_code'] == 422:
                pull_request['data'] = "Conflict whit the pull request. Please contact to support."
            response = {
                "success": pull_request['success'],
                "message": pull_request['data']
            }
            return Response(response, status=pull_request['status_code'])
        response = {
            "success": pull_request['success'],
            "message": "Pull Request was merged",
            "data": pull_request['data']
        }
        PullRequest.objects.filter(number=pull_number).update(status='merged')
        return Response(response, status=pull_request['status_code'])
    except Exception as e:
        logging.error(str(e))
        response = {
            "success": False,
            "message": "Something goes wrong. Please, contact to support."
        }
        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
