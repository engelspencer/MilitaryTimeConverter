time = input('Enter a military or civilian time: ')
conversion = ' '
splitlist1 = [' ' , ' ']
splitlist2 = [' ' , ' ']
milmath = 0
temptime = ' '

if (':' in time):
	if ('am' in time or 'Am' in time or 'aM' in time or 'AM' in time or 'a.m' in time or 'A.m' in time or 'a.m' in time or 'A.M' in time or 'am.' in time or 'Am.' in time or 'aM.' in time or 'AM.' in time or 'a.m.' in time or 'A.m.' in time or 'a.M.' in time or 'A.M.' in time):
		splitlist1 = time.split(':')
		if ("a" in splitlist1[1]):
			splitlist2 = splitlist1[1].split("a")
		elif ("A" in splitlist1[1]):
			splitlist2 = splitlist1[1].split("A")
		if (time[1] == ":" and (time[0] == "1" or time[0] == "2" or time[0] == "3" or time[0] == "4" or time[0] == "5" or time[0] == "6" or time[0] == "7" or time [0] == "8" or time[0] == "9") and (time[2] == "0" or time[2] == "1" or time[2] == '2' or time[2] == '3' or time[2] == '4' or time[2] == '5') and (time[3] == '0' or time[3] == '1' or time[3] == '2' or time[3] == '3' or time[3] == '4' or time[3] == '5' or time[3] == '6' or time[3] == '7' or time[3] == '8' or time[3] == '9')):
			conversion = "0" + splitlist1[0]+splitlist2[0]
		elif (time[0] == "1" and (time[1] == '0' or time[1] == '1' or time[1] == '2') and time[2] == ':' and (time[3] == 0 or time[3] == 1 or time[3] == 2 or time[3] == 3 or time[3] == 4 or time[3] == 5) and (time[4] == 0 or time[4] == 1 or time[4] == 2 or time[4] == 3 or time[4] == 4 or time[4] == 5 or time[4] == 6 or time[4] == 7 or time[4] == 8 or time[4] == 9)):
			if (splitlist1[0] == "12"):
				splitlist1[0] = "00"
			conversion = splitlist1[0] + splitlist2[0]
		else:
			print ('Error: unrecognized format')
		print (conversion)
	elif ("pm" in time or "Pm" in time or "pM" in time or "PM" in time or "p.m" in time or "P.m" in time or "p.M" in time or "P.M" in time or "pm." in time or "Pm." in time or "pM." in time or "PM." in time or "p.m." in time or "P.m." in time or "p.M." in time or "P.M." in time):
		splitlist1 = time.split(":")
		if ("p" in splitlist1[1]):
			splitlist2 = splitlist1[1].split("p")
		elif ("P" in splitlist1[1]):
			splitlist2 = splitlist1[1].split("P")
		if (time[0] == '1' and time[1] == '2' and time[2] == ':' and (time[3] == '0' or time[3] == '1' or time[3] == '2' or time[3] == '3' or time[3] == '4' or time[3] == '5') and (time[4] == '0' or time[4] == '1' or time[4] == '2' or time[4] == '3' or time[4] == '4' or time[4] == '5' or time[4] == '6' or time[4] == '7' or time[4] == '8' or time[4] == '9')):
			conversion = splitlist1[0] + splitlist2[0]
		elif (((time[0] == '1' or time[0] == '2' or time[0] == '3' or time[0] == '4' or time[0] == '5' or time[0] == '6' or time[0] == '7' or time[0] == '8' or time[0] == '9') and time[1] == ":" and (time[2] == '0' or time[2] == '1' or time[2] == '2' or time[2] == '3' or time[2] == '4' or time[2] == '5') and (time[3] == '0' or time[3] == '1' or time[3] == '2' or time[3] == '3' or time[3] == '4' or time[3] == '5' or time[3] == '6' or time[3] == '7' or time[3] == '8' or time[3] == '9')) or (time[0] == '1' and (time[1] == '0' or time[1] == '1' or time[1] == '2') and time[2] == ":" and (time[3] == '0' or time[3] == '1' or time[3] == '2' or time[3] == '3' or time[3] == '4' or time[3] == '5') and (time[4] == '0' or time[4] == '1' or time[4] == '2' or time[4] == '3' or time[4] == '4' or time[4] == '5' or time[4] == '6' or time[4] == '7' or time[4] == '8' or time[4] == '9'))):
			conversion = str(int(splitlist1[0] + splitlist2[0]) + 1200)
		else:
			print ('Error: unrecognized format')
		print (conversion)
elif ((time[0] == '0' or time[0] == '1' or time[0] == '2') and (time[1] == '0' or time[1] == '1' or time[1] == '2' or time[1] == '3' or time[1] == '4' or time[1] == '5' or time[1] == '6' or time[1] == '7' or time[1] == '8' or time[1] == '9') and (time[2] == '0' or time[2] == '1' or time[2] == '2' or time[2] == '3' or time[2] == '4' or time[2] == '5') and (time[3] == '0' or time[3] == '1' or time[3] == '2' or time[3] == '3' or time[3] == '4' or time[3] == '5' or time[3] == '6' or time[3] == '7' or time[3] == '8' or time[3] == '9')):
	splitlist1 = time.split()
	milmath = int(splitlist1[0])
	if (milmath == 0 or milmath == 2400):
		conversion = '12:00 am'
	elif (milmath >= 1 and milmath < 1000):
		if (milmath < 10):
			conversion = '12:0' + time[3] + ' am'
		elif (milmath < 100):
			conversion = '12:' + time[2] + time[3] + ' am'
		elif (milmath < 1000):
			conversion = time[1] + ':'  + time[2] + time[3] + ' am'
		else:
			print ('Error: unrecognized format')
	elif (milmath >= 1000 and milmath < 1200):
		conversion = time[0] + time[1] + ':' + time[2] + time[3] + ' am'
	elif (milmath >= 1200 and milmath < 1300):
		conversion = time[0] + time[1] + ':' + time[2] + time[3] + ' pm'
	elif (milmath >= 1300 and milmath < 2400):
		temptime = str(milmath - 1200)
		if (milmath < 2200):
			conversion = temptime[0] + ':' + temptime[1] + temptime[2] + ' pm'
		elif (milmath >= 2200):
			conversion = temptime[0] + temptime[1] + ':' + temptime[2] + temptime[3] + ' pm'
		else:
			print('Error: unrecognized format')
	else:
		print ('Error: unrecognized format')
	print (conversion)
else:
	print ("Error: unrecognized format")
