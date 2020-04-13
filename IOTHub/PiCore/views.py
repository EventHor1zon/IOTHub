from django.shortcuts import render, get_object_or_404

# Create your views here.

from . import models


class IndexView(ListView):
    
    def get(self, request):
        devices = models.Device.objects.all()
        return render(request, 'index.html')


class DeviceView(DetailView):
    
    def get(self, request, id):
        device = get_object_or_404(models.Device, pk=id)
        return render(request, 'devices.html', {"device":device})


class LEDView(DetailView):


    def get(self, request):
        devices = picore_models.Device.objects.filter(peripherals__ptype__exact="LED")
        spi_leds = devices.objects.filter(peripherals__connection_method__exact="SPI")
        rmt_leds = devices.objects.filter(peripherals__connection_method__exact="RMT")
        return render(request, 'ledctrl.html', {'devices':devices, 'spi_leds':spi_leds, 'rmt_leds':rmt_leds})

    def post(self, request):
        return