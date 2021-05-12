from rest_framework import serializers
from .models import ScrapModel

class ScrapSerializer(serializers.ModelSerializer):
   
    class Meta:
        fields = ('id','date', 'open_filed', 'hight_field', 'low_field', 'close_field', 'adj_close_field','volume_field' , 'name')
        model = ScrapModel