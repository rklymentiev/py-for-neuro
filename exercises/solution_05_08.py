import io
import numpy as np
import matplotlib.pyplot as plt
import requests
from PIL import Image

ID = 69750516 # subject ID
# API URL
URL = f"http://api.brain-map.org/api/v2/image_download/{ID}"
# additional parameters for request
params = {
    "quality": 50,
    "downsample": 2,
	"width": 5000,
	"height": 5000
	}

response = requests.get(URL, params=params)

# alternative way of request URL would be:
# URL = "http://api.brain-map.org/api/v2/image_download/69750516quality=50&downsample=2&width=5000&height=5000"

print(f"Status code: {response.status_code}")

# convert result binary image to numpy array
img = Image.open(io.BytesIO(response.content))
img = np.asarray(img)

# plot the image
plt.figure(figsize=(7,7), facecolor="white")
plt.imshow(img)
plt.axis("off")
plt.show()
