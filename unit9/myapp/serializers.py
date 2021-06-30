from myapp.models import Room, Door
from rest_framework import serializers

class RoomSerializer(serializers.Serializer):
    class Meta:
        model = Room
        fields = ('url', 'name', 'state', 'timestamp', 'pin')

class DoorSerializer(serializers.Serializer):
    class Meta:
        model = Door
        fields = ('url', 'name', 'state', 'timestamp', 'pin')