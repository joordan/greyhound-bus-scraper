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




odd = driver.find_elements_by_class_name("odd")
even = driver.find_elements_by_class_name("even")


a = np.array(odd)
b = np.array(even)



# interweave 2 list ex. [1,3] & [2,4] becomes [1,2,3,4]
c = np.empty((a.size + b.size,), dtype=a.dtype)
c[0::2] = a
c[1::2] = b




departures = c.tolist()

temparr = []

select = Select(driver.find_element_by_id('select-date-stop'))




for x in departures:

#	print(x.text) # has breaks

	#temparr is html row temparr[1] is location
	temparr = x.text.split(' ')
#separation needs to be done here

	for row in temparr:
		row = row.replace('\n',' ')
		outputfile.write(row)
		outputfile.write(' ')


	outputfile.write('\n') # start new line for each row


select = Select(driver.find_element_by_id('select-date-stop'))
options = len(select.options)


if (options > 1):


        select.select_by_index(1)
        tomorrow_deps = driver.find_elements_by_class_name("odd")
        even = driver.find_elements_by_class_name("even")








        if (even):
                a = np.array(tomorrow_deps)
                b = np.array(even)



                # interweave 2 list ex. [1,3] & [2,4] becomes [1,2,3,4]
                c = np.empty((a.size + b.size,), dtype=a.dtype)
                c[0::2] = a
                c[1::2] = b


                tomorrow_deps = c.tolist()


        nextday = []




        for x in tomorrow_deps:
                nextday = x.text.split(' ')


        for row in nextday:
                row = row.replace('\n',' ')
                outputfile.write(row)
                outputfile.write(' ')
driver.close()

