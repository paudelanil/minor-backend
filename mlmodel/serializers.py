from rest_framework import serializers
from .models import MlModel

class MlSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            "category",
        )
        model=MlModel