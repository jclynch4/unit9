from django.shortcuts import render
from myapp.models import Room, Door
from rest_framework import viewsets
from django.template import RequestContext
from myapp.serializers import RoomSerializer, DoorSerializer
import requests
import json
# Create your views here.

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class DoorViewSet(viewsets.ModelViewSet):
    queryset = Door.objects.all()
    serializer_class = DoorSerializer


def home(request):
    r = requests.get('localhost:8000/room/', auth=('username', 'password'))
    result = r.text
    output = json.loads(result)
    roomCount = output('count')

    r = requests.get('localhost:8000/door/', auth=('username', 'password'))
    result = r.text
    output = json.loads(result)
    doorCount = output('count')

    roomsDict={}

    for i in range (0, roomCount):
        r = requests.get('localhost:8000/room/' + str(i+1) +'/', auth=('username', 'password'))
        result = r.text
        output = json.loads(result)
        roomName = output['name']
        roomState = output['state']
        roomTimestamp = output['timestamp']
        roomsDict[roomName] = [roomState, roomTimestamp]

    doorsDict={}

    for i in range (0, doorCount):
        r = requests.get('localhost:8000/room/' + str(i+1) +'/', auth=('username', 'password'))
        result = r.text
        output = json.loads(result)
        doorName = output['name']
        doorState = output['state']
        doorTimestamp = output['timestamp']
        doorsDict[doorName] = [doorState, doorTimestamp]

    return render(request, 'myapp/index.html', context=RequestContext(request))