from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.authtoken.models import Token
from rest_framework.utils.representation import serializer_repr

from account.models import User
from account.pagination import AccountPagination
from account.serializers import AccountUserSerializer, LoginSerializer, RegisterSerializers
from rest_framework.generics import GenericAPIView


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountUserSerializer
    # permission_classes = (IsAdminUser,)
    pagination_class = AccountPagination


class LoginApi(GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)

        if not user:
            return Response({'detail': 'The user does not exist or incorrect password.'}, status.HTTP_401_UNAUTHORIZED)

        token, create = Token.objects.get_or_create(user=user)

        user_serializer = AccountUserSerializer(user, context={'request':request})

        data = {
            **user_serializer.data,
            'token': token.key
        }

        return Response(data)

class RegisterApi(GenericAPIView):

    serializer_class = RegisterSerializers

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token =  Token.objects.create(user=user)

        user_serializer = AccountUserSerializer(user, context={'request':request})

        data = {
            **user_serializer.data,
            'token': token.key
        }

        return Response(data)


