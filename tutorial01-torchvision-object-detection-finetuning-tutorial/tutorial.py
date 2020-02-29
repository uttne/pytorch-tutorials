# https://pytorch.org/tutorials/intermediate/torchvision_tutorial.html

import os
import numpy as np
import torch
from PIL import Image
import requests
from download import download
import zipfile

url = 'https://www.cis.upenn.edu/~jshi/ped_html/PennFudanPed.zip'
file_name = './PennFudanPed.zip'

root_dir = os.path.dirname(os.path.abspath(__file__))

# currnet dir change
os.chdir(root_dir)

download(url, file_name)

with zipfile.ZipFile(file_name) as exising_zip:
    exising_zip.extractall('./PennFudanPed')
