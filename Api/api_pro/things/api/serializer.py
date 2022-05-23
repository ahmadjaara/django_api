from rest_framework import serializers
from things.models import Thing

class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        fields=("id","name","description")
        model=Thing

 

# responsible to formate the data and arise error if there is an error in it 
