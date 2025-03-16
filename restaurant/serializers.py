from rest_framework.serializers import ModelSerializer
from .models import Booking, MenuItem

class BookingSerializer(ModelSerializer):
    class Meta:
        model =  Booking
        fields = '__all__'

class MenuItemSerializer(ModelSerializer):
    class Meta:
        model =  MenuItem
        fields = '__all__'        