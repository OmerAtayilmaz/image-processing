import cv2
import os


script_dir = os.path.dirname(os.path.abspath(__file__)) #week2 klasörünü verdi
proj_root = os.path.abspath(os.path.join(script_dir,os.pardir))

image_path = os.path.join(proj_root,'assets','bober.png')

image = cv2.imread(image_path)

if image is None:
    print("Check the path and try again!")

else:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray_image,100, 200)

    cv2.imshow('Original Image', image)
    cv2.imshow('Edge detection', edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()