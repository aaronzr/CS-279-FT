#
# Sources:
#
# Discrete 2D Fourier transform
# adapted from 1D DFT by Project Nayuki, 2017. Public domain.
# https://www.nayuki.io/page/how-to-implement-the-discrete-fourier-transform
# 
# Numpy image I/O
# adapted from 'filter.py' in Assignment 3
# by CS 279 course staff, 2017.
#

# 
# Computes the discrete Fourier transform (DFT) of the given complex vector.
# 'input' is a sequence of numbers (integer, float, or complex).
# Returns a list of complex numbers as output, having the same length.
# 
import cmath
import sys, os

def compute_dft_complex(input):
	n = len(input)
	output = []
	for k in range(n):  # For each output element
		s = complex(0)
		for t in range(n):  # For each input element
			angle = 2j * cmath.pi * t * k / n
			s += input[t] * cmath.exp(-angle)
		output.append(s)
	return output


# 
# (Alternate implementation using only real numbers.)
# Computes the discrete Fourier transform (DFT) of the given complex vector.
# 'inreal' and 'inimag' are each a sequence of n floating-point numbers.
# Returns a tuple of two lists of floats - outreal and outimag, each of length n.
 
#import math

#def compute_dft_real_pair(inreal, inimag):
#	assert len(inreal) == len(inimag)
#	n = len(inreal)
#	outreal = []
#	outimag = []
#	for k in range(n):  # For each output element
#		sumreal = 0.0
#		sumimag = 0.0
#		for t in range(n):  # For each input element
#			angle = 2 * math.pi * t * k / n
#			sumreal +=  inreal[t] * math.cos(angle) + inimag[t] * math.sin(angle)
#			sumimag += -inreal[t] * math.sin(angle) + inimag[t] * math.cos(angle)
#		outreal.append(sumreal)
#		outimag.append(sumimag)
#	return (outreal, outimag)

def main():
    usage = 'USAGE: python dft.py img1 [img2...]'
    if len(sys.argv) < 2:
        print usage
    for s in sys.argv[1:]:
        try:
            imgName = s
            if not os.path.exists(imgName):
                print usage
                print "Error: File %s does not exist"%imgName
                exit(1)
            
            # Reading in image
            img = plt.imread(imgName).astype(np.float64)
            if len(img.shape) > 2:
              print "Flattening image..."
              img = ndimage.imread(imgName, flatten=True)
            
            # Applying FT
            fImg = compute_dft_complex(img)
            
            # Printing image values to terminal
            print 'Original image: \n', img
            print 'Fourier image: \n', fImg
            
            # Using matplotlib to generate images colorbars
            plt.figure('original image')
            plt.imshow(img)
            plt.colorbar()
            plt.figure('filtered image')
            plt.imshow(fImg)
            plt.colorbar()
            plt.show()
    
        except:
            print 'Please use image files as input (*.jpg, *.png, *.bmp, *.gif, *.tif)'
            print usage
            exit(1)
        

# Boiler plate invokes the main function
if __name__ == "__main__":
    main()
