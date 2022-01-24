from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from companies.models import Company
from companies.serializers import CompanySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Company.objects.all().order_by('id')
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]