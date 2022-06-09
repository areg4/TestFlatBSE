from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Authors views
class Authors(APIView):
    
    def get(self, request, *args, **kwargs):
        return Response({"data": "ok"}, status=status.HTTP_200_OK)
