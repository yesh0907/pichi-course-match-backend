from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from pichicm_backend.profiles.models import Profile
from pichicm_backend.profiles.serializers import UpdateProfileSerializer


class RetreiveUpdateProfileApi(RetrieveUpdateAPIView):
    """
    Authenticated User can retreive his/her profile
    Authenticated User can update his/her profile
    """

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    serializer_class = UpdateProfileSerializer

    def _generate_successful_response(
        self, profile: Profile, status_code: int, message: str
    ) -> dict:
        return {
            "success": True,
            "status": status_code,
            "message": message,
            "data": {
                "user": {"id": profile.user.id, "email": profile.user.email},
                "student_year": profile.student_year,
                "phone_number": profile.phone_number,
            },
        }

    def _generate_unsuccessful_response(
        self, status_code: int, message: str, error: Exception
    ) -> dict:
        return {
            "success": False,
            "status": status_code,
            "message": message,
            "error": str(error),
        }

    def get(self, request):
        try:
            profile = Profile.objects.get(user=request.user)
            status_code = status.HTTP_200_OK
            response = self._generate_successful_response(
                profile=profile,
                status_code=status_code,
                message="Profile successfully fetched",
            )

        except Exception as e:
            status_code = status.HTTP_404_BAD_REQUEST
            response = self._generate_unsuccessful_response(
                status_code=status_code, message="Profile does not exists", error=e
            )

        return Response(data=response, status=status_code)

    def put(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        try:
            profile = Profile.objects.get(user=request.user)
            profile.student_year = validated_data.get(
                "student_year", profile.student_year
            )
            profile.phone_number = validated_data.get(
                "phone_number", profile.phone_number
            )
            profile.save()

            status_code = status.HTTP_200_OK
            response = self._generate_successful_response(
                profile=profile,
                status_code=status_code,
                message="Successfully updated User Profile",
            )

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = self._generate_unsuccessful_response(
                status_code=status_code, message="Profile does not exists", error=e
            )

        return Response(data=response, status=status_code)