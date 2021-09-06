import cv2
import numpy as np

qrCodeDetector = cv2.QRCodeDetector()
vid = cv2.VideoCapture(0)
while True:
	ret,frame=vid.read()
	cv2.imshow('frame',frame)
	decodedText, points, _ = qrCodeDetector.detectAndDecode(frame)
	if points is not None:
    # QR Code detected handling code
		print(decodedText)
	else:
    		print("QR code not detected")	
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break
vid.release()
cv2.destroyAllWindows()
