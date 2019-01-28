from datetime import datetime

currenttime = datetime.now()

filename = "output.txt"

inputfile = open(filename,"r",encoding='utf-8')
outputfile = open("filtered.txt","w+")


times = []

### example
### 6879 Sacramento, CA → Los Angeles, CA A12:15 pm D12:25 pm A12:11 pm D12:29 pm 
###


# for each line split it and grab the dep -3
# last element is /n



for line in inputfile:
	row = line.split(' ')
	row = row[:-9] + row[-3:-1]
	print(row)




