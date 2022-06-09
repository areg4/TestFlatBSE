from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


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
        return Response({"data": "ok"}, status=status.HTTP_200_OK)
    