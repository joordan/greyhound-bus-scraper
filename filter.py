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


prev_day = 'none'

for line in inputfile:
	row = line.split(' ')
	print('\nline:',line)
	print('dep:',row[-3])
	departure = row[-3]
#	print('departure')
#	print(departure)

	day = row[-2]


#	print('ampm:',day)

# get departure

	sdeparture = departure[1:3] + departure[4:6]
#	del departure[0]
#	del departure[2]

#	print('shortened')
#	print(sdeparture)


# same thing but remove ':'

#	print('int')
	depint = departure[1:3] + departure[4:6]
#	print(depint)

# destination from 2nd index to starting of time index

	destination = ' '.join(row[1:len(row)-9])
#	print(' '.join(destination))


# calculate minutes left

	time_now = currenttime.strftime('%-H:%M')


# print all
	print('bus#:',row[0])
	print('destination:',destination)
	print('dep:',departure[1:])
	print('current time:',time_now)





