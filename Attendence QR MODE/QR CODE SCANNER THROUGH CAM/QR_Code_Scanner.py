import cv2
from pyzbar.pyzbar import decode

capture = cv2.VideoCapture(0)
recieved_data = None # grab the default camera

while True:
    _, frame = capture.read()

    decoded_data = decode(frame) #These two lines of code is to get string from qr code
    try : 
        data =decoded_data[0][0]  # To get the string once only
        if data != recieved_data:
            print(data)
            recieved_data = data
    except:
        pass

    cv2.imshow('QR Code Scanner',frame)

    key = cv2.waitKey(1) # to remove the cam window for 1 millisecond
    
    if key ==ord('q'): #(To use escape button to remove the window)
        break
