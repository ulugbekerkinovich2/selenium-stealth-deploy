from rest_framework import serializers

from basic_app import models


class UploadDataSerialzier(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.UploadDatas
