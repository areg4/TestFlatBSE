import logging
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Utils.GitHubAPIRequests import GitHubAPIRequests
from .serializers import AuthorsSerializers


# Authors views
class Authors(APIView):
    """
        API to List Authors from the repo

        GET:
            summary: Endpoint to List Authors
            description: Get the list of the authors (collaborators) in the repo.
            responses:
                200: 
                    description: List the Authors
    """
    
    def get(self, request, *args, **kwargs):
        try:
            github_api_requests = GitHubAPIRequests()
            authors = github_api_requests.get_collaborators()
            if not authors['success']:
                response = {
                    "success" : authors['success'],
                    "message": authors['data']
                }
                return Response(response, status=authors['status_code'])
            authors_serializer = AuthorsSerializers(authors['data'], many=True)
            response = {
                "success" : authors['success'],
                "message": "List of the Authors",
                "data": authors_serializer.data
            }
            return Response(response, status=authors['status_code'])
        except Exception as e:
            logging.error(str(e))
            response = {
                "success": False,
                "message": "Something goes wrong. Please, contact to support."
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
