from django.shortcuts import render
from django.http import HttpResponse
import Home.templates
from django.template import loader
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from Home.serializers import UserSerializer, GroupSerializer

def show(request):
    return HttpResponse("Start")


def start(request):
    return HttpResponse("WAAAAGH!!!")


def render_template(request):
    return render(request, 'page1.html', {})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer