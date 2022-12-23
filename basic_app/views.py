from requests import Response
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from basic_app import models, serializers
from basic_app.models import UploadDatas


# Create your views here.
class CreateUploadData(generics.CreateAPIView):
    queryset = models.UploadDatas.objects.all()
    serializer_class = serializers.UploadDataSerialzier


class ListUploadData(generics.ListAPIView):
    queryset = models.UploadDatas.objects.all()
    serializer_class = serializers.UploadDataSerialzier


class DetailUploadData(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.UploadDatas.objects.all()
    serializer_class = serializers.UploadDataSerialzier


class ProfileList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        queryset = UploadDatas.objects.all()
        return Response({'data': queryset})


class ListLevel(generics.ListCreateAPIView):
    queryset = models.Mylevel.objects.all()
    serializer_class = serializers.MyLevelSerialzier


class DetailLevel(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Mylevel.objects.all()
    serializer_class = serializers.MyLevelSerialzier
