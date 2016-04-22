from scipy.misc import imsave,imread
import ipol.wrappers.Variational_Framework_for_Non_Local_Inpainting as wrapper
def example():
   
   from matplotlib import pyplot as plt
   import cv2
   im_file =wrapper.source_directory+'/data/kom07.png'
   mask_file =wrapper.source_directory+'/data/kom07_msk.png'
   image=imread(im_file)# the scipy.misc.imread uses PIL which give an error for this bmp file (Unsupported BMP compression )
   mask=cv2.imread(mask_file)# for some strange reason scipy.misc.imread is not able to read that image properly
   output=wrapper.inpaint(image,mask)
   plt.subplot(1,3,1)
   plt.imshow(image)
   plt.subplot(1,3,2)
   plt.imshow(mask)
   plt.subplot(1,3,3)
   plt.imshow(output)
   plt.show()
   print 'done' 
   
if __name__ == '__main__':
   #_install()
   example()
