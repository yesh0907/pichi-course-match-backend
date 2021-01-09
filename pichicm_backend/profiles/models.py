from django.db import models

from pichicm_backend.authentication.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    student_year = models.PositiveIntegerField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        return self

    def __str__(self):
        return self.user.email