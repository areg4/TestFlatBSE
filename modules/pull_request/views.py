import logging
from django.shortcuts import render
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
                200:
                    description: List the Pull Requests.
    """
    
    @swagger_auto_schema()
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
    
    
    @swagger_auto_schema()
    def post(self, request, *args, **kwargs):
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
        
        
@api_view(['GET'])
@swagger_auto_schema()
def pull_request_by_number(request, pull_number):
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
    
    
@api_view(['PUT'])
@swagger_auto_schema()
def merge_pull_request(request, pull_number):
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
