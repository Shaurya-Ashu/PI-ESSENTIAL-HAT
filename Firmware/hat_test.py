import time
import board
import busio
import digitalio
import neopixel

i2c = busio.I2C(board.SCL, board.SDA)

import adafruit_bno08x
from adafruit_bno08x.i2c import BNO08X_I2C
imu = BNO08X_I2C(i2c)
imu.enable_feature(adafruit_bno08x.BNO_REPORT_ACCELEROMETER)

import adafruit_vl53l4cx
tof = adafruit_vl53l4cx.VL53L4CX(i2c)
tof.start_ranging()

import adafruit_mcp9808
temp = adafruit_mcp9808.MCP9808(i2c)

import adafruit_veml7700
als = adafruit_veml7700.VEML7700(i2c)

import adafruit_tcs34725
color = adafruit_tcs34725.TCS34725(i2c)

import adafruit_lps2x
baro = adafruit_lps2x.LPS22(i2c)

import adafruit_inmp441
mic_spi = busio.SPI(board.SCK, board.MISO)
mic_cs = digitalio.DigitalInOut(board.D8)
mic = adafruit_inmp441.INMP441(mic_spi, mic_cs)

import adafruit_gps
import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
gps = adafruit_gps.GPS(uart)
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")

pixels = neopixel.NeoPixel(board.D18, 25, brightness=0.2)

pixels.fill((255, 0, 0))
time.sleep(0.5)
pixels.fill((0, 255, 0))
time.sleep(0.5)
pixels.fill((0, 0, 255))
time.sleep(0.5)
pixels.fill((0, 0, 0))

while True:
    accel = imu.acceleration
    print(f"IMU accel: x={accel[0]:.2f} y={accel[1]:.2f} z={accel[2]:.2f}")

    if tof.data_ready:
        print(f"ToF distance: {tof.distance} mm")

    print(f"Temp: {temp.temperature:.1f} C")
    print(f"Light: {als.lux:.1f} lux")

    r, g, b, c = color.color_raw
    print(f"Color R={r} G={g} B={b} C={c}")

    print(f"Pressure: {baro.pressure:.1f} hPa  Temp: {baro.temperature:.1f} C")

    gps.update()
    if gps.has_fix:
        print(f"GPS: {gps.latitude:.6f}, {gps.longitude:.6f}")
    else:
        print("GPS: no fix yet")

    pixels[0] = (0, 50, 0)
    time.sleep(0.1)
    pixels[0] = (0, 0, 0)

    print("---")
    time.sleep(1)
