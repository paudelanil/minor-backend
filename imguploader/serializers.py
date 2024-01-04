from rest_framework import serializers

from .models import Img

class ImgUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Img
        fields=["image"]