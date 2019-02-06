import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import Select

outputfile = open("output.txt","w+",encoding='utf-8')

options = webdriver.ChromeOptions()
options.add_argument('headless')


#driver = webdriver.Chrome()
driver = webdriver.Chrome(chrome_options=options)


#driver.get("https://www.google.com")
driver.get("http://63.247.92.82/stops/893740/Stockton_CA/arriving")

#driver.implicitly_wait(10)



#cheat count for Stockton
count = 0

odd = driver.find_elements_by_class_name("odd")
even = driver.find_elements_by_class_name("even")

print('odd')
print(odd)





a = np.array(odd)
b = np.array(even)



# interweave 2 list ex. [1,3] & [2,4] becomes [1,2,3,4]
c = np.empty((a.size + b.size,), dtype=a.dtype)
c[0::2] = a
c[1::2] = b




departures = c.tolist()

temparr = []

for x in departures:

#	print(x.text) # has breaks

	#temparr is html row temparr[1] is location
	temparr = x.text.split(' ')
	count = count + 1
	meridiem = temparr[-1] # [am|pm]
	print(meridiem)
#separation needs to be done here

	for row in temparr:
		row = row.replace('\n',' ')
		outputfile.write(row)
		outputfile.write(' ')

	# cheat for Stockton departure, remove for other cities/stops
	if (count > 6 and 'am' in meridiem):
		outputfile.write(' tomorrow')
	else:
		outputfile.write(' today')

	print(temparr)

	outputfile.write('\n') # start new line for each row


select = Select(driver.find_element_by_id('select-date-stop'))
select.select_by_index(1)
odd = driver.find_elements_by_class_name("odd")

nextday = []

print('\nTomorrow')



#for x in odd:
#	print(x.text)

for x in odd:
	nextday = x.text.split(' ')
	print(nextday)


	for row in nextday:
		row = row.replace('\n',' ')
		outputfile.write(row)
		outputfile.write(' ')
	outputfile.write(' tomorrow')



driver.close()


#print(even)
print(count,'deps')
