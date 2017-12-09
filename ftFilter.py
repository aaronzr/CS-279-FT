from scipy import ndimage
from scipy.misc import imsave
import numpy as np
import matplotlib.pyplot as plt
import cmath
import sys, os
import pdb


def main():
    usage = 'ftFilter.py: Convolves two images together via FFT.\nUSAGE: python ftFilter.py img1 img2'
    if len(sys.argv) < 2:
        print usage
        exit(1)
    imgNames = sys.argv[1:]
    imgs = []
    imgFT = []
    for imgName in imgNames:
        if not os.path.exists(imgName):
            print usage
            print "Error: File %s does not exist"%imgName
            exit(1)
        # Reading in image
        img = plt.imread(imgName).astype(np.float64)
        if len(img.shape) > 2:
            print "Flattening image..."
            img = ndimage.imread(imgName, flatten=True)
        # Record original image for later
        imgs.append(img)
    
    # Padding: expand each image to M + N - 1 in each dimension
    pdb.set_trace()
    dims = (imgs[0].shape[0] + imgs[1].shape[0] - 1, 
            imgs[0].shape[1] + imgs[1].shape[1] - 1)
    for i in range(len(imgs)):
        img = imgs[i]
        imgs[i] = np.lib.pad(img, ((0, dims[0] - img.shape[0]), (0, dims[1] - img.shape[1])), 'constant', constant_values=(0,))

    for img in imgs:
        # 2D FFT of the image
        fImg = np.fft.fft2(img)
        # Note: fImg is still complex-valued at this point
        imgFT.append(fImg)
    
    # Convolution in the spatial domain is elementwise
    # multiplication in the Fourier domain
    convFT = np.multiply(imgFT[0], imgFT[1])
    # Inverse FFT on the convolution
    conv = np.fft.ifft2(convFT)
    # Convert complex numbers to magnitudes
    fImg = np.array([[abs(c) for c in row] for row in conv])
        
    # Printing image values to terminal
    print 'Original image 1: \n', imgs[0]
    print 'Original image 2: \n', imgs[1]
    print 'Filtered image (FFT convolution): \n', fImg
    
    # Using matplotlib to generate images colorbars
    plt.figure('Original image 1')
    plt.imshow(imgs[0])
    plt.colorbar()
    plt.figure('Original image 2')
    plt.imshow(imgs[1])
    plt.colorbar()
    plt.figure('Fourier convolution')
    plt.imshow(fImg)
    plt.colorbar()
    plt.show()
    
# Boiler plate invokes the main function
if __name__ == "__main__":
    main()

