from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from pichicm_backend.authentication.serializers import (
    UserCreateSerializer,
    UserLoginSerializer,
)


class UserLoginApi(CreateAPIView):
    """Login a user and get back a JWT token"""

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        status_code = status.HTTP_200_OK
        response = {
            "success": True,
            "status": status_code,
            "message": "Successfully logged in User",
            "token": serializer.data['token'],
        }
        return Response(data=response, status=status_code)


class UserCreateApi(CreateAPIView):
    """Create a new user"""

    permission_classes = (AllowAny,)
    serializer_class = UserCreateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            "success": True,
            "status": status_code,
            "message": "Sucessfully created User",
            "data": serializer.data,
        }
        return Response(data=response, status=status_code)


class UserDestroyApi(DestroyAPIView):
    """
    De-activate User in order to keep user data
    """

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def destroy(self, request):
        try:
            user = request.user
            user.is_active = False
            user.save()

            status_code = status.HTTP_204_NO_CONTENT
            response = {
                "success": True,
                "status": status_code,
                "message": "User successfully deleted",
            }
        except Exception as e:
            status_code = status.HTTP_404_NOT_FOUND
            response = {
                "success": False,
                "status": status_code,
                "message": "User does not exist",
                "error": str(e),
            }

        return Response(data=response, status=status_code)