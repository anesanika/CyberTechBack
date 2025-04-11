from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True, required=True)

  class Meta:  # Capital M in Meta
    model = User
    fields = ["username", "password"]  # Must be a list of strings, not a single string

  def create(self, validated_data):
    user = User.objects.create_user(
      username=validated_data["username"],
      password=validated_data["password"]
    )
    return user
