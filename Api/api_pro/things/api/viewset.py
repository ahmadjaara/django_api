from rest_framework import generics
from .serializer import ThingSerializer
from things.models import Thing

class ThingsListApiView(generics.ListCreateAPIView):
    queryset=Thing.objects.all()
    serializer_class=ThingSerializer

class ThingsdetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Thing.objects.all()
    serializer_class=ThingSerializer