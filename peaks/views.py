from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from rest_framework import generics
from .serializers import PeakListSerializer
from .models import Peak
from gmplot import gmplot

# Create your views here.
class PeakListAPIView(generics.ListAPIView):
    queryset = Peak.objects.all()
    serializer_class = PeakListSerializer

class PeakCreateAPIView(generics.CreateAPIView):
    queryset = Peak.objects.all()
    serializer_class = PeakListSerializer

class PeakRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = "id"
    queryset = Peak.objects.all()
    serializer_class = PeakListSerializer

class PeakDestroyAPIView(generics.DestroyAPIView):
    lookup_field = "id"
    queryset = Peak.objects.all()

def destroy(request):
    queryset = Peak.objects.all().delete()
    return HttpResponseRedirect('/')

def map(request, id):
    queryset = Peak.objects.get(id=id)
    gmap = gmplot.GoogleMapPlotter(queryset.lat, queryset.lon, 5)
    gmap.marker(queryset.lat, queryset.lon, color='red')
    gmap.draw("templates/map.html")
    template = loader.get_template('map.html')
    return HttpResponse(template.render(request=request))

def ingest(request):
    Peak.objects.create(name='Mont Blanc', lat=45.832119, lon=6.865575, alt=4809.0)
    Peak.objects.create(name='Everest', lat=27.986065, lon=86.922623, alt=8849.0)
    return HttpResponseRedirect('/')