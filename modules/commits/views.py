from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


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
        return Response({"data": "ok"}, status=status.HTTP_200_OK)
    