from django.shortcuts import render
from rest_framework import generics

from basic_app import models, serializers
from file_yuklash import yukla


def index(request):
    return render(request, 'index.html')


# Create your views here.
class CreateUploadData(generics.CreateAPIView):
    queryset = models.UploadDatas.objects.all()
    serializer_class = serializers.UploadDataSerialzier

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


class ListUploadData(generics.ListAPIView):
    queryset = models.UploadDatas.objects.all()
    serializer_class = serializers.UploadDataSerialzier


class DetailUploadData(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.UploadDatas.objects.all()
    serializer_class = serializers.UploadDataSerialzier
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['input_level']


# class ProfileList(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'index.html'
#
#     def get(self, request):
#         queryset = UploadDatas.objects.all()
#         return Response({'data': queryset})

def yuklash():
    yukla()
