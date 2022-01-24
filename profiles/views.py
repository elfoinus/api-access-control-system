from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from profiles.models import Profile
from profiles.serializers import ProfileSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users profile to be viewed or edited.
    """
    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]