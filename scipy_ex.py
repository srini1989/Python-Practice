from scipy.misc import imread, imsave, imresize
# Read an JPEG image in to a numpy array
img = imread("../images/testImage.jpeg")
print(img.dtype, img.shape)

# Create a tinted image
img_tinted = img * [1, 0.95, 0.9]

# Use Image resize to resize an image
img_tinted = imresize(img_tinted, (300, 300))

# Write the modified image back
imsave("../images/testImage.jpeg")
