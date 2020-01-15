
#!/usr/bin/env python3.6
import os, sys
from PIL import Image
Image.MAX_IMAGE_PIXELS = None


def Tiff2JpegF(imInFolder="./imagesTIF/",imOutFolder="./imagesJPEG/"):
	listImages=os.listdir(imInFolder)
	for image in listImages:
		if image[-4:] == "tiff":
			im = Image.open(imInFolder+image)
			if im.mode!='RGB':
				im = im.covert('RGB')
			im.save(imOutFolder+image[:-4]+"jpeg")

def Tiff2Jpeg(image):
	im = Image.open(image)
	if im.mode!='RGB':
		im = im.convert('RGB')
	im.save(image[:-4]+"jpeg")



if __name__=="__main__":
	print(len(sys.argv))
	if len(sys.argv) == 2:
		Tiff2Jpeg(sys.argv[1])
	if len(sys.argv) == 3:
		Tiff2JpegF(sys.argv[1],sys.argv[2])


