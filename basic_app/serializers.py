from rest_framework import serializers

from basic_app import models
# from test1_automatic import selenium_upload


class UploadDataSerialzier(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.UploadDatas

    def create(self, validated_data):
        # selenium_upload()
        return self.validated_data
