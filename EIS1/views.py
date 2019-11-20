from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import data
# Create your views here.
@csrf_exempt
def test(request):
    if request.method == "POST":
        s = data()
        s.text = request.POST["data"]
        s.save()
        return HttpResponse("Data received")
    return HttpResponse("No Data sent")