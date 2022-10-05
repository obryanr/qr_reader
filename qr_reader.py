"""Main executor"""

import av
import cv2
import numpy as np
from pyzbar.pyzbar import decode

class VideoProcessor():
    def recv(self, frame):
        frm = frame.to_ndarray(format="bgr24")
        self.decoder(frm)
        return av.VideoFrame.from_ndarray(frm, format="bgr24")

    def decoder(self, image):
        """Decode QR Code"""
        gray_img = cv2.cvtColor(image, 0)
        barcode = decode(gray_img)

        for obj in barcode:
            points = obj.polygon
            (x, y, w, h) = obj.rect
            pts = np.array(points, np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(image, [pts], True, (0, 255, 0), 3)

            barcode_data = obj.data.decode("utf-8")
            barcode_type = obj.type
            string = "Data: " + str(barcode_data) + " | Type: " + str(barcode_type)

            cv2.putText(image, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255), 2)
            print("Barcode: "+barcode_data +" | Type: "+barcode_type)