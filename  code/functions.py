# Import requests, shutil python module.
import requests
import os

import shutil

def callYolo():
	main = "darknet.exe detect yolov3-voc.cfg .\\results_mine\\yolov3-voc_last.weights data\\streetview\\local_image0.jpg"
	r_v = os.system(main) 
	main = "darknet.exe detect yolov3-voc.cfg .\\results_mine\\yolov3-voc_last.weights data\\streetview\\local_image1.jpg"
	r_v = os.system(main) 
	print (r_v )

def getImg(location):
	# This is the image url.
	x = str(location[0])
	y = str(location[1])
	image_url0  = "https://maps.googleapis.com/maps/api/streetview?size=2048x2048&fov=120&location="+x+","+y+"&heading=0&key="
	image_url90 = "https://maps.googleapis.com/maps/api/streetview?size=2048x2048&fov=120&location="+x+","+y+"&heading=90&key="
	image_url180= "https://maps.googleapis.com/maps/api/streetview?size=2048x2048&fov=120&location="+x+","+y+"&heading=180&key="
	image_url270= "https://maps.googleapis.com/maps/api/streetview?size=2048x2048&fov=120&location="+x+","+y+"&heading=270&key="

	# Open the url image, set stream to True, this will return the stream content.
	resp0 = requests.get(image_url0, stream=True)
	resp1 = requests.get(image_url90, stream=True)
	resp2 = requests.get(image_url180, stream=True)
	resp3 = requests.get(image_url270, stream=True)


	# Open a local file with wb ( write binary ) permission.
	local_file0 = open('data/streetview/local_image0.jpg', 'wb')
	local_file1 = open('data/streetview/local_image1.jpg', 'wb')
	local_file2 = open('data/streetview/local_image2.jpg', 'wb')
	local_file3 = open('data/streetview/local_image3.jpg', 'wb')

	# Set decode_content value to True, otherwise the downloaded image file's size will be zero.
	resp0.raw.decode_content = True
	resp1.raw.decode_content = True
	resp2.raw.decode_content = True
	resp3.raw.decode_content = True

	# Copy the response stream raw data to local image file.
	shutil.copyfileobj(resp0.raw, local_file0)
	shutil.copyfileobj(resp1.raw, local_file1)
	shutil.copyfileobj(resp2.raw, local_file2)
	shutil.copyfileobj(resp3.raw, local_file3)


	#return [resp0.raw,resp1.raw,resp2.raw,resp3.raw]

	# Remove the image url response object.
	del resp0
	del resp1
	del resp2
	del resp3


def main():
	location = [42.350468, -71.110636]
	getImg(location)
	callYolo()

if __name__=="__main__":
	main()