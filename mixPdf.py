import sys, glob
from time import sleep
from datetime import datetime
from PyPDF2 import PdfFileReader, PdfFileWriter

monitorFolder = ""
outputFolder = ""

def mixPdf():
	filePath = glob.glob(monitorFolder + '/*.pdf')
	if(len(filePath) < 2): return
	try:
		
		oddFileName = filePath[-2].split("/")[-1].split(".")[0]
		evenFileName = filePath[-1].split("/")[-1].split(".")[0]
		odd = PdfFileReader(open(filePath[-2],'rb')).pages
		even = PdfFileReader(open(filePath[-1],'rb')).pages
		
		if (len(odd) - len(even) > 1) or (len(odd) < len(even)):
			return
			

		writer = PdfFileWriter()

		for i in range(0,len(odd)):
			writer.addPage(odd[i])
			if i < len(even):
				writer.addPage(even[-(i+1)])

		output = '{}/{}-{}-mixed.pdf'.format(outputFolder, oddFileName, evenFileName)
		writer.write(open(output, 'wb'))
		print("[{}] mixed file: {} & {}".format(datetime.now().isoformat(), oddFileName, evenFileName), file = sys.stdout)
		
		os.remove(filePath[-2])
		os.remove(filePath[-1])
	except Exception as e:
		print("[{}] Exceptation occurred: {} ".format(datetime.now().isoformat(), str(e)), file = sys.stdout)
		return


while(1):
	mixPdf()
	sleep(10)
