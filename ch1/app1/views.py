from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def MyFunction(request):
    return HttpResponse("Hello this is a home page")


def AliceInChains(request):
    song = " And yet i fight.. And yet i fight this battel all alone "
    return HttpResponse(song)
