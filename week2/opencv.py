import cv2 

import os #path yönetimi


#current directory
script_directory = os.path.dirname(os.path.abspath(__file__))
## klasöre eriştik 

#project rootuna eriştik
proj_root = os.path.abspath(os.path.join(script_directory,os.pardir))

#project rootundan assets içerisindeki bir görselin pathine eriştik
image_path = os.path.join(proj_root, 'assets','cat.png')

#image 
image = cv2.imread(image_path)
cv2.imshow('Cat Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

