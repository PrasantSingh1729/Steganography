from numpy.core.arrayprint import printoptions
from ImageSteg import ImageSteg
from PIL import Image
import pandas as pd
import numpy as np


img = ImageSteg()
img.encrypt_text_in_image("test.jpg","IT'S A SECRET MESSAGE","static/")
res = img.decrypt_text_in_image("static/test_encrypted.png")
print(res)
