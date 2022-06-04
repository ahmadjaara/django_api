from rest_framework import generics
from .serializer import ObjectSerializer
from app.models import ObjectModel

class ObjectsListApiView(generics.ListCreateAPIView):
    queryset=ObjectModel.objects.all()
    serializer_class=ObjectSerializer

class ObjectsdetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=ObjectModel.objects.all()
    serializer_class=ObjectSerializer