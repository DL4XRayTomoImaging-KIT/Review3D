from skimage import io
from reviews import *


im = io.imread("513.tif")
x = getView(view_type="planes")
x(im)
plt.show()