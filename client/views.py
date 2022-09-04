from django.shortcuts import render
from client.models import Client


def client(request):
    context = {}
    client_list = Client.objects.all()
    context['client_list'] = client_list
    return render(request, 'Client.html', context)