from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


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
        return Response({"data": "ok"}, status=status.HTTP_200_OK)
    