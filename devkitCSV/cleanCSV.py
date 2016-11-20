from sys import argv #To input file name. Usage: python cleanCSV.py file_name.csv

script, fileIn, fileOut = argv #unpacking  args. into variables

# Putting input file content into a string variable
initialFile = open(fileIn)
initialCsv = initialFile.read()
initialFile.close()

#Operations on the string
finalCsv = initialCsv.replace('"(', '[').replace(')"', ']')    \
.replace('array([[', '').replace(']]','').replace('dtype=','') \
.replace('uint8),', '').replace('uint16),', '').replace("array([u'", '') \
.replace("']", "").replace("'<U9')", "").replace(' ','').replace(',\n','')

#print finalCsv

#Writing that string to final file.
finalFile = open(fileOut, 'w')
finalFile.write(finalCsv)
finalFile.close()
