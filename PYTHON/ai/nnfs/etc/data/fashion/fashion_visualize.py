# console
import cv2
image_data = cv2.imread('fashion_mnist_images/train/3/0002.png', cv2.IMREAD_UNCHANGED)
#print(image_data)

# image
import matplotlib.pyplot as plt

# for blue-yellow
plt.imshow(image_data)

# gray sale
#plt.imshow(image_data, cmap='gray')

plt.show()
