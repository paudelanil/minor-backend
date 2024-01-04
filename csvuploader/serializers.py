from rest_framework import serializers
from .models import File

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

class SaveFileSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            "id",
            "name",
            "position",
            "age",
        )
        model=File
        