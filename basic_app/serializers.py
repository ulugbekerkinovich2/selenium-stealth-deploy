from rest_framework import serializers

from basic_app import models
from basic_app.models import UploadDatas


class UploadDataSerialzier(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.UploadDatas

    def create(self, validated_data):
        return UploadDatas.objects.create(**validated_data)
