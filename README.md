# PI-ESSENTIAL-HAT
It's a like a sense HAT but on steroids with sensors,GPS module and a RGB matrix . It can sense acceleration, orientation, pressure ,temperature ,luminosity ,color  ,audio, and map surrounding.
Compatible with raspberry pie 5,4,3 Zero & Zero W .

# Zine 

<img width="540" height="828" alt="Frame 5" src="https://github.com/user-attachments/assets/7497351b-4302-4809-9738-eb416ddf5887" />


# Why i built this 
I have a raspberry pi 4 on me and wanted a hat for it which could provide like all in one pack and so i built one for it , taking a little inspiration from snese hat .

# Schematics 
I have used EASY EDA for shecmatics and PCB designing 

1st Sensor is BNO080 a Advance IMU which does all the heavy math internally — it gives you ready-to-use orientation, rotation vectors, and acceleration without needing to fuse raw sensor data. It's the same kind of chip used in high-end VR headsets and drones so we could use this hat in devlopment of similar tech . 
The interface is I2C.
<img width="688" height="421" alt="Screenshot 2026-06-21 at 4 03 12 AM" src="https://github.com/user-attachments/assets/3d688864-50b9-42e4-bb4d-9cff4040c984" />


2nd Sensor is 3DToF or should i say a Mini LiDAR VL53L9CXV0VE/1 ,it fires invisible infrared light pulses and measures how long they take to bounce back, giving you distances up to 1 meter. It's the kind of tech used in phone face-unlock systems like our iphone face id (maybe) . it's the most expensive part also 
The interface is I2C
<img width="364" height="404" alt="Screenshot 2026-06-21 at 4 06 23 AM" src="https://github.com/user-attachments/assets/aec451ce-a1c4-4feb-9da0-c89c3a0caa16" />


Then we have a Barometer LPS22HHTR it measure change in pressure to estimate height , used in drones etc. The interface is I2C and also I had also added a logic level shifter .
<img width="556" height="191" alt="Screenshot 2026-06-21 at 4 08 49 AM" src="https://github.com/user-attachments/assets/2bc5914b-cd07-4f5d-9421-a7d034bc6daa" />
<img width="174" height="245" alt="Screenshot 2026-06-21 at 4 10 16 AM" src="https://github.com/user-attachments/assets/354b544a-7be6-4740-9847-bc08a0d4cd3c" />


Then we have separate temperature sensor MCP9808 , It comunicate in I2C giving one of the most accurate temperature with the difference of +-0.25°C .and also I had also added a logic level shifter .
<img width="240" height="131" alt="Screenshot 2026-06-21 at 4 13 33 AM" src="https://github.com/user-attachments/assets/b3652d02-f42f-4c71-a0d4-3de1f88aa24d" />
<img width="228" height="282" alt="Screenshot 2026-06-21 at 4 13 41 AM" src="https://github.com/user-attachments/assets/b9b77965-b559-4fd4-8122-934e3b9e1126" />


Then we have our 5th sensor i.e. Ambient Light Sensor (ALS) VEML7700 also with a I2C interface and on eof the simples connection .
<img width="233" height="229" alt="Screenshot 2026-06-21 at 4 15 49 AM" src="https://github.com/user-attachments/assets/3147a495-732d-4aef-81e1-a35463074b70" />


The 6th sensor is a MIC yeah a MEMS Microphone INMP441 but with I2S protocal which drirectly gives digital out put so no adc required .
<img width="332" height="146" alt="Screenshot 2026-06-21 at 4 17 52 AM" src="https://github.com/user-attachments/assets/d67485da-e5f7-48ad-a647-155d13feea96" />


The last one is Color Sensor TCS34725FN also a I2C interface with directly tell you the color of the surface it is faced to in RGB value . I have add a dedicated led for lighting the sugject .
<img width="394" height="159" alt="Screenshot 2026-06-21 at 4 20 40 AM" src="https://github.com/user-attachments/assets/529e34c2-aea7-41d0-ad31-5ed990a532ab" />


There are other things also like a GPS module and a 5x5 RGB Matrix .
The GPS Module is a L76X with UART communication and a active anntena is required for its working .
<img width="479" height="345" alt="Screenshot 2026-06-21 at 4 23 12 AM" src="https://github.com/user-attachments/assets/c4e8ac83-3cec-43f6-90d9-d668bbef0721" />

The GPS Module is a L76X with UART communication and a active anntena is required for its working .
<img width="573" height="294" alt="Screenshot 2026-06-21 at 4 22 52 AM" src="https://github.com/user-attachments/assets/5a7bc514-45fb-406d-afaf-a34499e3a086" />


# PCB 
There are 4 layer but i could have easy done it in 2 layes but i didn't want to disterb the GPS module and tracing every vcc and gnd so i used 4 layer's with confi of 
Top - Signal
Inner1 - GND
Inner2 - VCC
Bottom - Signal

<img width="545" height="488" alt="Screenshot 2026-06-21 at 4 26 23 AM" src="https://github.com/user-attachments/assets/60e1b7f9-b6c2-47a8-a8ac-7ffa1cb1fba3" />
<img width="544" height="473" alt="Screenshot 2026-06-21 at 4 26 35 AM" src="https://github.com/user-attachments/assets/63544afe-a330-4943-9d31-ee98075ddfe9" />
<img width="524" height="468" alt="Screenshot 2026-06-21 at 4 26 46 AM" src="https://github.com/user-attachments/assets/0b563411-906b-4472-8059-5ac548c17672" />
<img width="529" height="466" alt="Screenshot 2026-06-21 at 4 26 56 AM" src="https://github.com/user-attachments/assets/8098ee08-62ee-4f90-91f8-b8e34dd14373" />



<img width="2160" height="1914" alt="2D_PCB1_2026-06-21" src="https://github.com/user-attachments/assets/2606330d-7de3-40fc-8b36-8f423158f739" />
<img width="2160" height="1914" alt="2D_PCB1_2026-06-21 (1)" src="https://github.com/user-attachments/assets/32a43c80-7203-4cf7-8161-0fd3b09d8af2" />


# Rendering

 I used Fusion 360 for this 
 
<img width="2880" height="1226" alt="Untitled_2026-Jun-20_07-31-18PM-000_CustomizedView25204277747_png_alpha" src="https://github.com/user-attachments/assets/f21ed17f-b8ab-460a-b0b9-d4c3a3e35357" />

<img width="3300" height="2550" alt="Untitled_2026-Jun-20_07-35-18PM-000_CustomizedView23587820129_png_alpha" src="https://github.com/user-attachments/assets/34c6c0f8-0f0e-4823-a5d7-22baed0c0fda" />

<img width="2880" height="1226" alt="Untitled_2026-Jun-20_07-32-05PM-000_CustomizedView16117473721_png_alpha" src="https://github.com/user-attachments/assets/72562075-6f47-44c6-b563-1fe0c25f375a" />


<img width="3300" height="2550" alt="Untitled_2026-Jun-20_07-37-06PM-000_CustomizedView16313768629_png_alpha" src="https://github.com/user-attachments/assets/670f1390-e8da-4d70-b583-276d8515cdb2" />


# Firmware 
 it a very simple test script written in python 
 Quick install on pi before running:
 
pip install adafruit-circuitpython-bno08x adafruit-circuitpython-vl53l4cx adafruit-circuitpython-mcp9808 adafruit-circuitpython-veml7700 adafruit-circuitpython-tcs34725 adafruit-circuitpython-lps2x adafruit-circuitpython-gps adafruit-circuitpython-neopixel adafruit-circuitpython-inmp441


