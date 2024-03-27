# fashion MNIST images download zip and unzip

from zipfile import ZipFile
import os
import urllib
import urllib.request

Url = 'https://nnfs.io/datasets/fashion_mnist_images.zip'
File = 'fashion_mnist_images.zip'
Folder = 'fashion_mnist_images'

if not os.path.isfile(File):
    print(f'Downloading {Url} and saving as {File}...')
    urllib.request.urlretrieve(Url, File)

print('Unzipping images...')
with ZipFile(File) as zip_images:
    zip_images.extractall(Folder)

print('Done')
