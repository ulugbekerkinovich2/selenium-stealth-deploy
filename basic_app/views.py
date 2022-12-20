from rest_framework import generics

from basic_app import models, serializers
from test1_automatic import selenium_upload


# Create your views here.
class CreateUploadData(generics.CreateAPIView):
    queryset = models.UploadDatas.objects.all()
    serializer_class = serializers.UploadDataSerialzier

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) and selenium_upload()

    # def get_queryset(self):
    #     selenium_upload()
    #     print('ishladi post')
    #     return models.UploadDatas.objects.all()


class ListUploadData(generics.ListAPIView):
    queryset = models.UploadDatas.objects.all()
    serializer_class = serializers.UploadDataSerialzier


class DetailUploadData(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.UploadDatas.objects.all()
    serializer_class = serializers.UploadDataSerialzier
