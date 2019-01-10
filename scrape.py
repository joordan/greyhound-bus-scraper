import numpy as np
from selenium import webdriver

outputfile = open("output.txt","w+",encoding='utf-8')

options = webdriver.ChromeOptions()
options.add_argument('headless')


#driver = webdriver.Chrome()
driver = webdriver.Chrome(chrome_options=options)


#driver.get("https://www.google.com")
driver.get("http://63.247.92.82/stops/893740/Stockton_CA/arriving")

#driver.implicitly_wait(10)


odd = driver.find_elements_by_class_name("odd")
even = driver.find_elements_by_class_name("even")




a = np.array(odd)
b = np.array(even)
c = np.empty((a.size + b.size,), dtype=a.dtype)

c[0::2] = a
c[1::2] = b

departures = c.tolist()

temparr = []

for x in departures:

#	print(x.text) # has breaks

	temparr = x.text.split(' ')
	print(temparr[1])

#separation needs to be done here

	for row in temparr:
		row = row.replace('\n',' ')
		outputfile.write(row)
		outputfile.write(' ')

	print(temparr)

	outputfile.write('\n') # start new line for each row


driver.close()
