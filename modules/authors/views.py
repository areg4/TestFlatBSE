from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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
        return Response({"data": "ok"}, status=status.HTTP_200_OK)
