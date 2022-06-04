from rest_framework import serializers
from app.models import ObjectModel

class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields=("id","name","description")
        model=ObjectModel

 

# responsible to formate the data and arise error if there is an error in it 
