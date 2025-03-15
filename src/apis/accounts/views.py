from http.client import HTTPResponse

from django.contrib import auth
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView



class Accounts(APIView):
    def get(self, request):
        accunts = User.objects.all()

        return Response({'accounts': accunts})

    def post(self, request):
        user = auth.authenticate(username=request.data['username'], password=request.data['password'])