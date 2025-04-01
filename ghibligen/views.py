from django.http import HttpResponse
from django.shortcuts import render


def gen(request):
    return render(request,"gen.html")

def vieww(request):
    return render(request,"view_image.html")