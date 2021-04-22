from machine import Pin, ADC, I2C, SPI,PWM
from time import sleep_ms
import machine
import gc
import random
from st7789 import ST7789,color565
from time import sleep_ms

MOSI_Pin = 19  #mosi pin
SCLK_Pin = 18  #clock pin
CS_Pin = 5     #chip select pin
DC_Pin = 16    #data/command pin
RST_Pin = 23
BL_Pin = 4     #backlight pin

# sda 21
# scl 22
# adc_in 34
# btn_1 35
# btn_2 0
# adc_power 14

spi=SPI(2, baudrate=4000000, polarity=1, phase=1, sck=Pin(SCLK_Pin), mosi=Pin(MOSI_Pin))

display=ST7789(spi,
        reset=Pin(RST_Pin, Pin.OUT),
        dc=Pin(DC_Pin, Pin.OUT),
        cs=Pin(CS_Pin, Pin.OUT),
        backlight=Pin(BL_Pin, Pin.OUT),
        rotation=3)# 0-Portrait, 1-Landscape, 2-Inverted Portrait,3-Inverted Landscape

display.fill(0)
display.pixel(50,50,color565(255,0,0))
display.pixel(60,60,color565(0,255,0))
display.pixel(70,70,color565(0,0,255))
