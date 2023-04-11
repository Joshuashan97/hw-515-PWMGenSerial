import serial
import sys
import time


def connectTest(ser1_name):
    print ("TESTING CONNECTION")
    try :
        ser1 = serial.Serial(ser1_name, 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, timeout = 2.5)
        
    except :
        error_message = "VFD SERIAL CABLE COMMUNICATION ERROR"


    print('Connected')
    return ser1

def setsignal(unit,var1,var2,device):

    t = 0.2
    if(unit==1):
        device.write(str.encode("S1F{}T".format(var1)))
        time.sleep(t)
        device.write(str.encode("S1D{:03d}T".format(var2)))
    elif(unit==2):    
        device.write(str.encode("S2F{}T".format(var1)))
        time.sleep(t)
        device.write(str.encode("S2D{:03d}T".format(var2)))
    return
    
    

def main():
    
    u = int(sys.argv[1])
    f1 = float(sys.argv[2])
    d1 = int(sys.argv[3])
    print("PWM:%d"%(u))
    print("Frequency:%.1f"%(f1))
    print("DutyCycle:%d"%(d1))
    serDevice = connectTest('/dev/ttyS0')
    setsignal(u,f1,d1,serDevice)

if __name__ == "__main__":
    main()
    exit(0)
        


        
     