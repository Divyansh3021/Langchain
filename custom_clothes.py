import cv2
import numpy as np

# Load the image
image = cv2.imread('input_image.jpg')

# Define the color you want the t-shirt to be
new_color = (0, 255, 255)  # BGR color code (here, red)

# Define the range of colors to replace (for the existing t-shirt color)
lower_range = (20, 20, 20)  # Lower range of color in BGR format (usually black)
upper_range = (60, 60, 60)  # Upper range of color in BGR format (adjust as needed)

# Create a mask to identify the t-shirt color in the image
mask = cv2.inRange(image, lower_range, upper_range)

# Replace the t-shirt color with the new color
image[mask > 0] = new_color

# Save the modified image
cv2.imwrite('output_image.jpg', image)

# Display the modified image (optional)
cv2.imshow('Modified Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
