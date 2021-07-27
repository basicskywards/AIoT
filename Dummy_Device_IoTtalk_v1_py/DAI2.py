import time, random, requests
import DAN

import serial
import time

ServerURL = 'https://4.iottalk.tw/'      #with non-secure connection
#ServerURL = 'https://DomainName' #with SSL connection
Reg_addr = None #if None, Reg_addr = MAC address

DAN.profile['dm_name']='Dummy_Device' # device model name (Jetson Nano)
DAN.profile['df_list']=['Dummy_Sensor', 'Dummy_Control',]
#DAN.profile['d_name']= 'Assign a Device Name' 

DAN.device_registration_with_retry(ServerURL, Reg_addr)
#DAN.deregister()  #if you want to deregister this device, uncomment this line
#exit()            #if you want to deregister this device, uncomment this line



class Arduino:
    def __init__(self):
        self.obj = serial.Serial("/dev/ttyUSB1", 9600, timeout=1)
        print("Arduino Connected")

    def left(self):
        self.obj.write(b'1')

    def right(self):
        self.obj.write(b'2')

obj = Arduino()

while True:
    try:
        IDF_data = random.uniform(1, 10)
        DAN.push ('Dummy_Sensor', IDF_data) #Push data to an input device feature "Dummy_Sensor"

        #==================================
        # you can also use Remote_Control (from iottalk) to send data to 'Dummy_Control' of 'Dummy_Device' (Jetson Nano)
        ODF_data = DAN.pull('Dummy_Control')#Pull data from an output device feature "Dummy_Control"
        if ODF_data != None:
            print (ODF_data[0])

            #==== Add code to control Servo from IoTTalk here ====#
            if int(ODF_data[0]/255.0) == 1:
                #obj.left()
                #time.sleep(5)
                print('\nAC ON!!!')
                obj.left()
                time.sleep(5)
                #print('right')
                #obj.right()
            
            #====#





            #==== Add code to control Servo from AI here ====#


            #=====#




            #==== Add code to control Servo from Temperature sensor here ====#


            #=====#




    except Exception as e:
        print(e)
        if str(e).find('mac_addr not found:') != -1:
            print('Reg_addr is not found. Try to re-register...')
            DAN.device_registration_with_retry(ServerURL, Reg_addr)
        else:
            print('Connection failed due to unknow reasons.')
            time.sleep(1)    

    time.sleep(0.2)

