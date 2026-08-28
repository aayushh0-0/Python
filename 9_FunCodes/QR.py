#import qrcode #library importeed for the QR
#data=input("Enter the Data for the Generation of QR code ~ \n")
#qr=qrcode.make(data) #function for making the QR with the data provided
#qr.save("qrcode.png")
#print("QR code Generated Succesfully")
import qrcode
data=input("Enter the data for the Generation of the QR Code ~ ")
qr=qrcode.make(data)
qr.save("QR.png")
print("QR Code Generated Succesfully!!!")