from django.urls import path
from .views import FaceDetectorView


urlpatterns = [
    path('facedetect/', FaceDetectorView.as_view(), name="facedetect"),
]
