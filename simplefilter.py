import csv
from datetime import datetime as dt
from datetime import timedelta
import datetime
import time

#Gets current datetime and reformats it into 'Year-Month-Date Hour:Minute AM/PM'
currentDateTime = dt.now()
currentOverallDateString = currentDateTime.strftime('%Y-%m-%d %I:%M %p')
currentOverallDate = datetime.datetime.strptime(currentOverallDateString, "%Y-%m-%d %I:%M %p")
#This is for the scraped datetime
formatYMD = currentDateTime.strftime('%Y-%m-%d')

#Used for testing
faketime = "2019-02-06 10:40 AM"
faketime = datetime.datetime.strptime(faketime, "%Y-%m-%d %I:%M %p")

#Opens txt file containg scraped data
filename = "output.txt"
inputfile = open(filename,"r",encoding='utf-8')
outputfile = open("filtered.txt","w+")
outputcsv = open("data.csv", "w")
wr = csv.writer(outputcsv,dialect='excel')

#For out of bounds exception
times = ["Start"]
dates = ["Start"]
schedule = ["Start"]

header = ["Schedule", "Origin and Destination", "Departure"]
wr.writerow(header)

#FOR OUTPUT.TXT
for index, line in enumerate(inputfile):
	row = line.split(' ')
	row = row[:-9] + row[-3:-1]
	time = row[-2]
	time = time[1:]
	row[-2] = time + " " + row[-1]
	del row[-1]
	row[1] =' '.join(row[1:-1])
	del row[2:-1]
	row[2] = row[2].replace("*", "")
	line = row
# 	print(line)


#FOR OUTPUT2.TXT
#Filters the scraped data and takes out unneeded information
# for index, line in enumerate(inputfile):
# 	row = line.split(' ')
# 	row = row[:-8] + row[-3:-1]
# 	time = row[-1] + " " + row[-2]
# 	time = time[1:]
# 	row[-2] = time
# 	del row[-1]
# 	row[1] =' '.join(row[1:-1])
# 	del row[2:-1]
# 	row[2] = row[2].replace("*", "")
# 	line = row	
# 	row = line.split(' ')
# 	row = row[:-8] + row[-2:]
# 	time = " ".join(row[-2:])
# 	time = time[1:]
# 	row[-2] = time
# 	del row[-1]
# 	row[1] =' '.join(row[1:-1])
# 	del row[2:-1]
# 	row[2] = row[2].replace("*", "")
# 	row[2] = row[2].replace("\n", "")
# 	line = row

	#Takes scraped time and adds the current Year-Month-Day
	depart_string = formatYMD + " " + row[2]
	depart_time = datetime.datetime.strptime(depart_string, "%Y-%m-%d %I:%M %p")
	depart_period = depart_time.strftime('%p')
	
	#Appends "AM/PM" to times, appends bus datetimes to dates, appends whole schedule.
	times.append(depart_period)
	dates.append(depart_time)
	schedule.append(line)

#For out of bounds exception
times.append("End")
dates.append("End")
schedule.append("End")

#(For adjustDays and for loop) Checks to see if list schedule changes from today 
#to tomorrow and adjusts for tomorrow
def adjustDays(forInd):
	for index, line in enumerate(times):
		if times[index+forInd] == "Start":
 			continue
		if times[index+forInd] == "End":
			break
		else:
			dates[index+forInd] = dates[index+forInd] + timedelta(days=1)
	return dates

for index, line in enumerate(times):
	if times[index] == "Start":
 		continue
	if times[index] == "End":
		break
	elif (times[index] == "AM" and times[index-1] == "PM"): 
		adjustDays(index)

#If current time pasts bus schedule, then writes remaining schedule into a CSV
for index, line in enumerate(schedule):
	if dates[index] == "Start":
 		continue
	if times[index] == "End":
		break
	elif dates[index] >= currentOverallDate:
		print(schedule[index])
		wr.writerow(schedule[index])
		



