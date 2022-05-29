from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from .serializers import UserModelSerializer
from django.contrib.auth.models import User


class UserViewSet(viewsets.ViewSet):
    """
    UserViewSet for creating/retrieving user
    """
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


    def list(self, request):
        queryset = User.objects.all()
        serializer_class = UserModelSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer_class = UserModelSerializer(post)
        return Response(serializer_class.data)

    def create(self, request):
        user_data = request.data
        serializer_class = UserModelSerializer(data=user_data)
        if serializer_class.is_valid():
            password = serializer_class.validated_data.get('password')
            serializer_class.validated_data['password'] = make_password(password)
            serializer_class.save()
            return Response({'message': 'User Registered'}, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {
                    'message': 'User Not Registered',
                    "Error": serializer_class.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass