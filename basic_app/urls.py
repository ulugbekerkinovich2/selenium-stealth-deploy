from django.urls import path

from basic_app import views

urlpatterns = [
    path('upload/', views.ListUploadData.as_view()),
    path('upload/<int:pk>', views.DetailUploadData.as_view()),
    path('uploads/', views.CreateUploadData.as_view()),
    path('user/', views.ProfileList.as_view()),
]
