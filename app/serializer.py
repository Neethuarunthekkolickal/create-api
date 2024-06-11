from rest_framework import serializers
from . models import Data

class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model=Data
        fields=['id','name','address']