import matplotlib.pyplot as plt
import numpy as np
import math
import serial

ser = serial.Serial(
        # Serial Port to read the data from
        port='COM5',
 
        #Rate at which the information is shared to the communication channel
        baudrate = 115200,
   
        #Applying Parity Checking (none in this case)
        parity=serial.PARITY_NONE,
 
       # Pattern of Bits to be read
        stopbits=serial.STOPBITS_ONE,
     
        # Total number of bits to be read
        bytesize=serial.EIGHTBITS,
 
        # Number of serial commands to accept before timing out
        timeout=1
)
# Pause the program for 1 second to avoid overworking the serial port
Data = []
T = np.arange(0,8192*525*10**-6,525*10**-6)
print(T)
count = 0
while 1:
        x=ser.readline()
        for line in x:
            if line == 45:
                Data.append(1)
            elif line == 95:
                Data.append(0)
        print(Data,len(Data))
        if(Data):
            if count == 0:
                Y1 = np.array(Data)
                Data = []
            else:
                Y2 = np.array(Data)
                Data = []
            count+=1
            if count==1:
                fig, ax = plt.subplots(1, 1)
                ax.set_title("BOOT Button")
                #ax[1].set_title("LED")
                ax.plot(T,Y1) #row=0, column=0
                #ax[1].plot(T,Y2) #row=1, column=0
                fig.tight_layout()
                plt.show()
                count = 0
                #break

ser.close()
        
