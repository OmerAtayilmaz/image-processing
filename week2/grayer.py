import cv2
import os


dosya_path = os.path.abspath(__file__)
klasor = os.path.dirname(dosya_path)
project_root = os.path.abspath(os.path.join(klasor,os.pardir))
images = os.path.join(project_root,'assets')

file_names = [f for f in os.listdir(images) if os.path.isfile(os.path.join(images, f))]


def grayify_image(img_name):
    image_path = os.path.join(project_root, 'assets',img_name)
    image = cv2.imread(image_path)
    if image is None:
        print("Failed to load the image.")
    else:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Original Image', image)
        cv2.imshow('Grayscale Image', gray_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def print_images():
    for index,file_name in enumerate(file_names):
        print(f"{index}-{file_name}")


print_images()

u_image_name = str(input("Which image do you want to pick? type it's full name:\n"))
grayify_image(u_image_name)