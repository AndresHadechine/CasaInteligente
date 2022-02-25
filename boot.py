from machine import Pin
import bluetooth
from BLE import BLEUART

#Init LEDs
pin0 = Pin(0, Pin.OUT) #Habitacion 1
pin2 = Pin(2, Pin.OUT) #Habitacion 2
pin4 = Pin(4, Pin.OUT) #Habitacion 3
pin5 = Pin(5, Pin.OUT) #Habitacion 4
pin22 = Pin(22, Pin.OUT) #Exterior 1
pin23 = Pin(23, Pin.OUT) #Exterior 2

#Init Fan, ventilador

Pin18 = Pin(18, Pin.OUT) #Ventilador

#Init Bluetooth
name = 'ESP32'
ble = bluetooth.BLE()
uart = BLEUART(ble, name)

#Bluetooth RX event
def on_rx():
    rx_buffer = uart.read().decode().strip()

    uart.write('ESP32 says: + ' str(rx_buffer) + '\n')

    #Encender habitaciones
    if rx_buffer == 'o':
        pin0.on() #Enciende habitación1
    if rx_buffer == 'q':
        pin2.on() #Enciende habitación2
    if rx_buffer == 's':
        pin4.on() #Enciende habitación3
    if rx_buffer == 'u':
        pin5.on() #Enciende habitación4

    #Apagar habitaciones
    if rx_buffer == 'p':
        pin0.off() #Apagar habitación1
    if rx_buffer == 'r':
        pin2.off() #Apagar habitación2
    if rx_buffer == 't':
        pin4.off() #Apagar habitación3
    if rx_buffer == 'v':
        pin5.off() #Apagar habitación4

    #Encender exterior
    if rx_buffer == 'k':
        pin22.on() #Enciende Exterior 1
    if rx_buffer == 'm':
        pin23.on() #Enciende Exterior 2

    #Apagar exterior
    if rx_buffer == 'n':
        pin22.off() #Enciende Exterior 1
    if rx_buffer == 'l':
        pin23.off() #Apaga Exterior 2

    #Encender ventilador
    if rx_buffer == 'a':
        pin18.off() #Enciende Ventilador
    if rx_buffer == 'b':
        pin18.off() #Apaga Ventilador

#Register Bluetooth event
uart.irq(handler=on_rx)