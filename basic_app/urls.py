from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from basic_app import views

urlpatterns = [
    path('upload/', views.ListUploadData.as_view()),
    path('upload/<int:pk>', views.DetailUploadData.as_view()),
    path('', views.CreateUploadData.as_view()),
    # path('', views.index),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
