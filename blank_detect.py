import sys, os, subprocess
import re
from pdf2image import convert_from_path 
from PIL import Image 

def pdf2image():
	# Path of the pdf 
	PDF_file = "example-new.pdf"

	# Store all the pages of the PDF in a variable 
	pages = convert_from_path(PDF_file, 500) 

	# Counter to store images of each page of PDF to image 
	image_counter = 1

	# Iterate through all the pages stored above 
	for page in pages: 

		filename = "page_"+str(image_counter)+".jpg"
		
		# Save the image of the page in system 
		page.save("pdf2images/"+filename, 'JPEG') 

		# Increment the counter to update filename 
		image_counter = image_counter + 1
	blank(image_counter)


def blank(image_count):
	for i in range(1,image_count):
		print("For page number",i)
		command = "identify -verbose pdf2images/page_"+str(i)+".jpg |grep 'standard deviation'"
		#result stores the output of the command line in a bytes array
		result =subprocess.check_output(command, shell = 'True')

		#result now contains a byte array, to convert it to string we use result.decode
		result = result.decode('utf-8')
		#print(result)

		#finds all the standard deviations for each colour channel
		result2 = re.findall("\s*standard deviation:\s*\d+\.\d+\s*\((?P<percent>\d+\.\d+)\).*", result)
		print("Standard deviations for all colour channels:", result2)

		#using only the last value, since that is the overall standard deviation
		if(len(result2) > 0):
			if(float(result2[3]) > 0.1):
				print("Not a Blank image")
				print("--------------------------------------")
			else:
				print("Blank image")
				print("--------------------------------------")
		else:
			print("Blank Image")
			print("--------------------------------------")

def main():
	pdf2image()


if __name__ == '__main__':
	main()