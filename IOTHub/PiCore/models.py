from django.db import models

# Create your models here.

CONNECT_METHOD = (
    ("LAN", "Local Area Network"),
    ("WLAN", "Wireless Local Area Network"),
    ("RMT", "rmt_driver")
    ("I2C", "i2c"),
    ("SPI", "SPI"),
    ("UART", "UART"),
    ("CAN", "CAN bus")
    ("LORA", "LoRa")
    ("BTLE", "BT Low Energy")
    ("JSON", "Json")
)




class Device(models.Model):

    class Meta:
        managed = True
        verbose_name = 'DeviceModel'
        verbose_name_plural = 'DeviceModels'
    
    # DEVICE_TYPES = (
    #     ("ESP32", "ESP 32"),
    #     ("RPIB", "Raspberry Pi B"),
    #     ("ATMEGA2560", "Arduino Mega 2560"),
    #     ("STM32F0", "STM32 F Zero"),
    #     ("RPI4", "Raspberry Pi 4"),
    #     ("RPIZW", "Raspberry Pi Zero W")
    # )

    
    device_name = models.CharField(max_length=50)
    device_type = models.CharField(max_length=100)
    device_state = models.BooleanField()
    uptime = models.TimeField(auto_now=False, auto_now_add=True)
    extensions = models.CharField(max_length=50, choices=CONNECT_METHOD)
    core_speed = models.IntegerField(verbose_name="speed")
    architecture = models.CharField(max_length=50)
    picture = models.ImageField()
    peripherals = models.ForeignKey("Peripheral", on_delete=models.CASCADE)
    ip_address = models.IPAddressField()


class Peripheral(models.Model):
    ## use this as a parent class to build device specific 
    ## models, or as blank class for filler  

    ADDRESSABLE_LEDS = "LED"
    SENSOR = "SEN"
    EMITTER = "EMT"
    RECEIVER = "RCV"

    PERIPHERAL_TYPE = [
    (ADDRESSABLE_LEDS, "addressable led"),
    (SENSOR, "sensor"),
    (EMITTER, "emitter"),
    (RECEIVER, "receiver")
    ]

    def __str__(self):
        pass

    class Meta:
        managed = True
        verbose_name = 'Peripheral'
        verbose_name_plural = 'Peripherals'

    p_state = models.BooleanField()
    p_type = models.models.CharField(max_length=3, choices=PERIPHERAL_TYPE)
    connection_method = models.CharField(max_length=50, choices=CONNECT_METHOD)
    max_speed = models.BigIntegerField()
    p_address = modles.IntegerField()


    def write_to(self, data):
        return 

    def read_from(self, data):
        return

    def set_state(self, state):
        return
