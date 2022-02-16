from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2

def decode(im) :
  # Menemukan Barcode dan QR code
  decodedObjects = pyzbar.decode(im)

  # Mencetak hasil
  for obj in decodedObjects:
    print('Type : ', obj.type)
    print('Data : ', obj.data,'\n')

  return decodedObjects

# Menampilkan lokasi barcode dan qrcode
def display(im, decodedObjects):

  for decodedObject in decodedObjects:
    points = decodedObject.polygon

    # Apabila tidak ditemukan quad, temukan convex hull
    if len(points) > 4 :
      hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
      hull = list(map(tuple, np.squeeze(hull)))
    else :
      hull = points;

    # jumlah titik pada convex hull
    n = len(hull)

    # Gambar convex hull
    for j in range(0,n):
      cv2.line(im, hull[j], hull[ (j+1) % n], (255,0,0), 3)

  # Menampilkan hasil
  cv2.imshow("Results", im);
  cv2.waitKey(0);

# Main
if __name__ == '__main__':

  # Read image
  im = cv2.imread('KSM 16521377 Semester 2 Tahun 20212022.jpg')

  decodedObjects = decode(im)
  display(im, decodedObjects)