from skimage import io
from fish_convert_crop import *

im = io.imread("513.tif")
x = get_views(view_types=["planes","slices"])
x(im)
plt.show()