time = "07:52:52PM"

#pre: time is a string in "HH:MM:SSAM" format
#post: convert to military time
def convertTime(time):
	hour = int(time[0:2])
	min = time[3:5]
	sec = time[6:8]
	if hour != 12 and time[8:10] == “PM”:
		hour += 12
	if hour == 12 and time[8:10] == “AM”:
		hour = 0
	if hour < 10:
		hour = “0” + str(hour)
	print(str(hour) + “:” + min + “:” + sec)
