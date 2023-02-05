import json
from django.shortcuts import render
from django.utils.safestring import mark_safe



def index(request):
    template_name = 'chat/index.html'
    context = {}
    return render(request, template_name, context)


def room(request, room_name):
    template_name = "chat/room.html"
    context = {"room_name_json": mark_safe(json.dumps(room_name))}
    return render(request, template_name, context)
