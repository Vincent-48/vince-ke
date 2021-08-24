# Just press run to get a random image.

from urllib import request

# Random image
api_call = "https://picsum.photos/200"
request.urlretrieve(api_call, "img.png")