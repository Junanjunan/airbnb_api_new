from django.core import serializers
from django.http import HttpResponse
from rooms.models import Room


def list_rooms(request):
    data = serializers.serialize("json", Room.objects.all())    # serializers.serialize(format, queryset)
    response = HttpResponse(content=data)
    return response