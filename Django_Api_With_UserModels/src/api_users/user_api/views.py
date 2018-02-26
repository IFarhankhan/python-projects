from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer 
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from . import serializers 
from . import models 
from . import permissions 
# Create your views here.

""" testing get method """
class TestApiView(APIView):
  
  """testing serializer views """
  Serializer_class = serializers.TestSerializer

  def get(self, request, format=None):
    """Advantage: allows you to control your logic"""
    an_apiview = []
    return Response({'message': 'Its working', 'an_apiview': an_apiview})

  def post(self, request):
    Serializer = serializers.TestSerializer(data=request.data)
    if Serializer.is_valid():
      name = Serializer.data.get('name')
      message = 'Testing {0}'.format(name)
      return Response({'message': message})
    else:
      return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk=None):
    return Response({'method': 'put'})

  def patch(self, request, pk=None):
    return Response({'method': 'patch'})
  
  def delete(self, request, pk=None):
    return Response({'method': 'delete'})
 


class TestViewSets(viewsets.ViewSet):
  
  Serializer_class = serializers.TestSerializer 

  def list(self, request):
    as_viewset = [
      'Maps without hustle URLS using routers, Common action: List, create',
      'retrieve, update'
    ]
    return Response({'message': 'Test', 'as_viewset': as_viewset})
  
  def create(self, request):
    Serializer = serializers.TestSerializer(data=request.data)
    if Serializer.is_valid():
      name = Serializer.data.get('name')
      message = 'test {0}'.formate(name)
      return Response({'message': message})
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def retrieve(self, request, pk=None):
    return Response({'http_method': 'GET'})
  
  def update(self, request, pk=None):
    return Response({'http_method': 'PUT'})

  def partial_update(self, request, pk=None):
    return Response({'http_method': 'PATCH'})

  def destroy(self, request, pk=None):
    return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
  
  serializer_class = serializers.UserProfileSerializer
  queryset = models.UserProfile.objects.all()
  authentication_classes = (TokenAuthentication,)
  permission_classes = (permissions.UpdateOwnProfile,)
  filter_backends = (filters.SearchFilter,)
  search_fields = ('name', 'email',)

class LoginViewSet(viewsets.ViewSet):
  serializer_class = AuthTokenSerializer
  
  def create(self, request):
   return ObtainAuthToken().post(request)

class UserProfileFeedViewSet(viewsets.ModelViewSet):
  authentication_classes = (TokenAuthentication,)
  serializer_class = serializers.ProfileFeedItemSerializer 
  queryset = models.ProfileFeedItem.objects.all()
  permission_classes = (permissions.PostOwnStatus, IsAuthenticated)
  
  def perform_create(self, serializer):
   serializer.save(user_profile=self.request.user)

