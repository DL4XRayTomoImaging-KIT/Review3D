from skimage import io
from fish_convert_crop import *

im = io.imread("513.tif")
x = getViews(view_types=["planes","slices"])
x(im)
plt.show()