import io
import numpy as np
import matplotlib.pyplot as plt
import requests
from PIL import Image

ID = ___ # subject ID
# API URL
URL = "http://api.brain-map.org/api/v2/image_download/"
# additional parameters for request
params = {
    "quality": ___,
    "downsample": ___,
	"width": ___,
	"height": ___
	}

response = ___.___(___, ___=___)
print(f"Status code: {___}")

# convert result binary image to numpy array
img = Image.open(io.BytesIO(response.content))
img = np.asarray(img)

# plot the image
plt.figure(figsize=(7,7), facecolor="white")
plt.imshow(img)
plt.axis("off")
plt.show()
