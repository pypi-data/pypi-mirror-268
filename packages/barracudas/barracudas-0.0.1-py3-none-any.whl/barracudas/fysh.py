import requests
from urllib import parse
# Import the necessary libraries
import serial
import time

def fysh(port, g_limit, token, chat_id, delay):

    # Define the serial port and baud rate
    #port = 'COM4'  # Replace 'COM4' with the appropriate port for your Arduino
    port = '/dev/ttyACM0' #R Pi
    baud_rate = 9600

    # Create a serial connection
    ser = serial.Serial(port, baud_rate)

    # Wait for the Arduino to reset
    time.sleep(2)

    # Read the data from the Arduino
    n = 0
    while True:
        data = ser.readline().decode('utf-8').strip()
        if n < 5:
            n += 1
            print(n)
        else:
            print(data)
            #####
            data_list = data.split(':')

            color_temp = int(data_list[1].split('K')[0])
            lux = int(data_list[2].split('-')[0])
            r = int(data_list[3].split('G')[0])
            g = int(data_list[4].split('B')[0])
            b = int(data_list[5].split('C')[0])
            c = int(data_list[6])
            
            g_ratio = g / (r+g+b)
            print(g_ratio)
            #####
            if g_ratio > g_limit:
                token = "6412873457:AAEguukJSGSSUw3U9WJk4SHlEDw8L4zicaE"
                chat_id = "-1002017139292"
                #"1500026181" me "-1002017139292" chanel
                message = f"<It's time to clean the fish tank!> \n Green: {g_ratio} \n Lux: {lux}"
                encode_message = parse.quote(message)
                url = 'http://api.telegram.org/bot' + token + '/sendmessage?chat_id=' + chat_id + '&text=' + encode_message
                response = requests.get(url)
                print(g_ratio, 'sent')
                n = -5
                time.sleep(delay)
        # Add a delay to reduce the CPU usage
        time.sleep(0.5)

    # Close the serial connection
    ser.close() 
