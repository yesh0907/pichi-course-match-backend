from rest_framework import serializers

from pichicm_backend.profiles.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "student_year",
            "phone_number",
        )


class UpdateProfileSerializer(serializers.Serializer):
    student_year = serializers.IntegerField(required=False)
    phone_number = serializers.CharField(required=False)