from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class ContactView(APIView):
    def get(self, request,contact_id):
        fakeContact = {
            "full_name": "Alejandro",
            "id": contact_id,
            "email":"my@email.com"
        }
        return Response(fakeContact)