from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

app_name = "addresses"


class AddressViewSet(viewsets.ModelViewSet):
    def post(self):
        pass