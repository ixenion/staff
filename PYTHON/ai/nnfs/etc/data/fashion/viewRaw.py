import cv2
'''# image preprocessing
image_data = cv2.imread('tshirt.png', cv2.IMREAD_UNCHANGED)

# to view the raw color image
import matplotlib.pyplot as plt
plt.imshow(cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB))
plt.show()

# to view the raw grayscaled image
image_data = cv2.imread('tshirt.png', cv2.IMREAD_GRAYSCALE)
import matplotlib.pyplot as plt
plt.imshow(cv2.cvtColor(image_data, cmap='gray'))
plt.show()'''

# to view the resized grayscaled image
image_data = cv2.imread('tshirt.png', cv2.IMREAD_GRAYSCALE)
image_data = cv2.resize(image_data, (28,28))
import matplotlib.pyplot as plt
plt.imshow(image_data, cmap='gray')
plt.show()
